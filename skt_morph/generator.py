from .analyzer import _get_db_connection
from .sandhi import apply_upasarga_sandhi
from .declension import decline_noun

def conjugate(dhatu_id, upasarga="", lakara="law", purusha="praTama", derivative="base", prayoga="kartari", voice="parasmEpadam"):
    """Fetches conjugation. If missing, dynamically generates via Upasarga sandhi."""
    conn = _get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT eka, dvi, bahu FROM conjugations 
        WHERE dhatu_id=? AND upasarga=? AND derivative=? AND prayoga=? AND lakara=? AND voice=? AND purusha=?
    """, (dhatu_id, upasarga, derivative, prayoga, lakara, voice, purusha))
    row = cursor.fetchone()
    
    if row:
        conn.close()
        return {"eka": row["eka"], "dvi": row["dvi"], "bahu": row["bahu"]}
        
    # FALLBACK: Generate Dynamically
    cursor.execute("""
        SELECT eka, dvi, bahu FROM conjugations 
        WHERE dhatu_id=? AND upasarga='' AND derivative=? AND prayoga=? AND lakara=? AND voice=? AND purusha=?
    """, (dhatu_id, derivative, prayoga, lakara, voice, purusha))
    base_row = cursor.fetchone()
    conn.close()
    
    if not base_row: return None
    
    return {
        "eka": apply_upasarga_sandhi(upasarga, base_row["eka"]),
        "dvi": apply_upasarga_sandhi(upasarga, base_row["dvi"]),
        "bahu": apply_upasarga_sandhi(upasarga, base_row["bahu"])
    }

def get_participle_declension(dhatu_id, pratyaya, gender, upasarga="", derivative="base"):
    """Fetches base participle, attaches Upasarga, and dynamically declines into 24 cases."""
    conn = _get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT base_form FROM participles 
        WHERE dhatu_id=? AND upasarga=? AND derivative=? AND pratyaya=?
    """, (dhatu_id, upasarga, derivative, pratyaya))
    row = cursor.fetchone()
    
    base_form = row["base_form"].split(',')[0] if row else None
    
    if not base_form:
        cursor.execute("""
            SELECT base_form FROM participles 
            WHERE dhatu_id=? AND upasarga='' AND derivative=? AND pratyaya=?
        """, (dhatu_id, derivative, pratyaya))
        base_row = cursor.fetchone()
        if not base_row: 
            conn.close()
            return None
        bare_base = base_row["base_form"].split(',')[0]
        base_form = apply_upasarga_sandhi(upasarga, bare_base)

    conn.close()
    return decline_noun(base_form, gender)
