import os
import sqlite3
from .sandhi import get_upasarga_splits
from .stemmer import get_stems
from .namadhatu import analyze_namadhatu

HOME_DIR = os.path.expanduser("~")
DB_PATH = os.path.join(HOME_DIR, ".skt_morph", "skt_morphology.db")

def _get_db_connection():
    if not os.path.exists(DB_PATH):  # pragma: no cover
        from .db_builder import build_database_if_missing
        print("Database not found. Rebuilding...")
        build_database_if_missing()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  
    return conn

def _extract_exact_matches(row, word, columns):
    matched = []
    for col in columns:
        if row[col]:
            forms = [f.strip() for f in row[col].split(',')]
            if word in forms:
                matched.append(col)
    return matched

def _is_valid_participle(conn, dhatu_id, upasarga, pratyaya):
    if pratyaya == 'lyap' and upasarga == "": return False
    if pratyaya in ['SAnac', 'cAnaS', 'sya-SAnac', 'BAvakarma-SAnac', 'sya-BAvakarma-SAnac']:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM conjugations WHERE dhatu_id = ? AND upasarga = ? AND voice = 'Atmanepadam' LIMIT 1", (dhatu_id, upasarga))
        if not cursor.fetchone(): return False 
    return True

def _fetch_verbs_from_db(word_slp1):
    conn = _get_db_connection()
    cursor = conn.cursor()
    search_term = f"%{word_slp1}%"
    cursor.execute("SELECT dhatu_id, upasarga, derivative, prayoga, lakara, voice, purusha, eka, dvi, bahu FROM conjugations WHERE eka LIKE ? OR dvi LIKE ? OR bahu LIKE ?", (search_term, search_term, search_term))
    raw_results = cursor.fetchall()
    
    results = []
    for row in raw_results:
        for vacana in _extract_exact_matches(row, word_slp1, ['eka', 'dvi', 'bahu']):
            results.append({
                "type": "verb", "dhatu_id": row["dhatu_id"], "upasarga": row["upasarga"],
                "derivative": row["derivative"], "prayoga": row["prayoga"], "lakara": row["lakara"], 
                "voice": row["voice"], "purusha": row["purusha"], "vacana": vacana
            })
    conn.close()
    return results

def analyze_verb(word_slp1):
    results = _fetch_verbs_from_db(word_slp1)
    if not results:
        for upa, stripped in get_upasarga_splits(word_slp1):
            sub_results = _fetch_verbs_from_db(stripped)
            for res in sub_results:
                if res["upasarga"] == "":  
                    res["upasarga"] = upa
                    res["note"] = "Dynamically matched via Sandhi split"
                    results.append(res)
            if results: break 
    return results

def _fetch_participles_from_db(word_slp1):
    conn = _get_db_connection()
    cursor = conn.cursor()
    search_term = f"%{word_slp1}%"
    cursor.execute("SELECT dhatu_id, upasarga, derivative, pratyaya, base_form, masculine, feminine, neuter FROM participles WHERE base_form LIKE ? OR masculine LIKE ? OR feminine LIKE ? OR neuter LIKE ?", (search_term, search_term, search_term, search_term))
    raw_results = cursor.fetchall()
    
    results = []
    avyaya_pratyayas = ['tumun', 'ktvA', 'lyap', 'Ramul']
    
    for row in raw_results:
        if not _is_valid_participle(conn, row["dhatu_id"], row["upasarga"], row["pratyaya"]): continue
        pratyaya = row["pratyaya"]
        matched_cols = _extract_exact_matches(row, word_slp1, ['base_form', 'masculine', 'feminine', 'neuter']) 
        for col in matched_cols:
            res = {
                "type": "avyaya" if pratyaya in avyaya_pratyayas else "participle",
                "dhatu_id": row["dhatu_id"], "upasarga": row["upasarga"], "derivative": row["derivative"],
                "pratyaya": pratyaya, "base_form": row["base_form"]
            }
            if col in ['masculine', 'feminine', 'neuter']:
                res["gender"] = col; res["case"] = "prathama"; res["vacana"] = "eka"
            else:
                res["note"] = "Matched uninflected base form"
            results.append(res)
            
    conn.close()
    return results

def analyze_participle_base(word_slp1):
    results = _fetch_participles_from_db(word_slp1)
    if not results:
        for upa, stripped in get_upasarga_splits(word_slp1):
            sub_results = _fetch_participles_from_db(stripped)
            for res in sub_results:
                if res["upasarga"] == "": 
                    res["upasarga"] = upa
                    res["note"] = "Dynamically matched via Sandhi split"
                    results.append(res)
            if results: break
    return results

def analyze_declension(word_slp1):
    guessed_stems = get_stems(word_slp1)
    results = []
    conn = _get_db_connection()
    cursor = conn.cursor()
    
    for guess in guessed_stems:
        stem = guess["stem"]
        search_term = f"%{stem}%"
        cursor.execute("SELECT dhatu_id, upasarga, pratyaya, base_form FROM participles WHERE base_form LIKE ?", (search_term,))
        db_matches = cursor.fetchall()
        exact_matches = [row for row in db_matches if stem in [s.strip() for s in row["base_form"].split(',')]] 
                
        if exact_matches:
            for row in exact_matches:
                results.append({
                    "type": "declension", "base_form": stem, "gender": guess["gender"], "case": guess["case"], "vacana": guess["vacana"],
                    "dhatu_id": row["dhatu_id"], "upasarga": row["upasarga"], "pratyaya": row["pratyaya"]
                })
        else:
            found_dynamic = False
            for upa, stripped_stem in get_upasarga_splits(stem):
                cursor.execute("SELECT dhatu_id, pratyaya, base_form FROM participles WHERE base_form LIKE ? AND upasarga = ''", (f"%{stripped_stem}%",))
                dyn_matches = cursor.fetchall()
                exact_dyn = [r for r in dyn_matches if stripped_stem in [s.strip() for s in r["base_form"].split(',')]]
                if exact_dyn:
                    for r in exact_dyn:
                        results.append({
                            "type": "declension", "base_form": stem, "gender": guess["gender"], "case": guess["case"], "vacana": guess["vacana"],
                            "dhatu_id": r["dhatu_id"], "upasarga": upa, "pratyaya": r["pratyaya"], "note": "Dynamic Upasarga Match"
                        })
                    found_dynamic = True
                    break
            
            if not found_dynamic:
                results.append({
                    "type": "declension", "base_form": stem, "gender": guess["gender"], "case": guess["case"], "vacana": guess["vacana"],
                    "dhatu_id": None, "upasarga": None, "pratyaya": None
                })
            
    conn.close()
    return results

def analyze(word_slp1):
    return {
        "verbs": analyze_verb(word_slp1),
        "participles": analyze_participle_base(word_slp1),
        "declensions": analyze_declension(word_slp1),
        "namadhatus": analyze_namadhatu(word_slp1)
    }
