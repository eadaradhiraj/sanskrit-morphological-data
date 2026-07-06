import os
import sqlite3
import json

# --- PATHS ---
# This locates the 'json_data' folder bundled right next to this script inside the package
PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_DIR = os.path.join(PACKAGE_DIR, "json_data")

# This is where the SQLite database will be built on the user's machine
HOME_DIR = os.path.expanduser("~")
APP_DIR = os.path.join(HOME_DIR, ".skt_morph")
DB_PATH = os.path.join(APP_DIR, "skt_morphology.db")

def create_schema(cursor):
    """Creates the unified database schema with high-performance indexes."""
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS info (
            id INTEGER PRIMARY KEY AUTOINCREMENT, dhatu_id TEXT, key_name TEXT, value TEXT
        );
        CREATE TABLE IF NOT EXISTS conjugations (
            id INTEGER PRIMARY KEY AUTOINCREMENT, dhatu_id TEXT, upasarga TEXT, 
            derivative TEXT, prayoga TEXT, lakara TEXT, voice TEXT, 
            purusha TEXT, eka TEXT, dvi TEXT, bahu TEXT
        );
        CREATE TABLE IF NOT EXISTS participles (
            id INTEGER PRIMARY KEY AUTOINCREMENT, dhatu_id TEXT, upasarga TEXT, 
            derivative TEXT, pratyaya TEXT, base_form TEXT, 
            masculine TEXT, feminine TEXT, neuter TEXT
        );
        CREATE TABLE IF NOT EXISTS upasarga_meanings (
            id INTEGER PRIMARY KEY AUTOINCREMENT, dhatu_id TEXT, 
            upasarga_combination TEXT, meaning TEXT
        );
        CREATE TABLE IF NOT EXISTS upasargachandrika (
            id INTEGER PRIMARY KEY AUTOINCREMENT, dhatu_id TEXT, upasarga_combination TEXT, 
            meaning TEXT, example_number TEXT, example_text TEXT, source TEXT
        );
        CREATE TABLE IF NOT EXISTS prayoga (
            id INTEGER PRIMARY KEY AUTOINCREMENT, dhatu_id TEXT, 
            form TEXT, lakara TEXT, purusha TEXT, vacana TEXT, book TEXT, literature_text TEXT
        );
        
        -- Indexes for lightning fast reverse-lookups
        CREATE INDEX IF NOT EXISTS idx_info_dhatu ON info(dhatu_id);
        CREATE INDEX IF NOT EXISTS idx_conj_eka ON conjugations(eka);
        CREATE INDEX IF NOT EXISTS idx_conj_dvi ON conjugations(dvi);
        CREATE INDEX IF NOT EXISTS idx_conj_bahu ON conjugations(bahu);
        CREATE INDEX IF NOT EXISTS idx_part_base ON participles(base_form);
    """)

def populate_database(conn):
    """Iterates over the bundled JSON files and inserts them into SQLite."""
    cursor = conn.cursor()
    print("Initializing skt-morph Engine. Compiling local database (this takes a few seconds)...")

    # Walk through the json_data folder (and its subfolders like 1/, 8/)
    for root, _, files in os.walk(JSON_DIR):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        print(f"Warning: Could not read {file}")
                        continue
                        
                dhatu_id = data.get("dhatu_id")
                if not dhatu_id: continue

                # 1. Info Table
                for key, val in data.get("info", {}).items():
                    cursor.execute("INSERT INTO info (dhatu_id, key_name, value) VALUES (?, ?, ?)", 
                                   (dhatu_id, key, val))

                # 2. Upasarga Meanings
                for um in data.get("upasarga_meanings", []):
                    cursor.execute("INSERT INTO upasarga_meanings (dhatu_id, upasarga_combination, meaning) VALUES (?, ?, ?)",
                                   (dhatu_id, um.get("combination", ""), um.get("meaning", "")))

                # 3. Upasargachandrika
                for uc in data.get("upasargachandrika", []):
                    cursor.execute("""
                        INSERT INTO upasargachandrika (dhatu_id, upasarga_combination, meaning, example_number, example_text, source) 
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (dhatu_id, uc.get("upasarga_combination", ""), uc.get("meaning", ""), 
                          uc.get("example_number", ""), uc.get("example_text", ""), uc.get("source", "")))

                # 4. Conjugations
                for c in data.get("conjugations", []):
                    cursor.execute("""
                        INSERT INTO conjugations (dhatu_id, upasarga, derivative, prayoga, lakara, voice, purusha, eka, dvi, bahu)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (dhatu_id, c.get("upasarga", ""), c.get("derivative", ""), c.get("prayoga", ""), 
                          c.get("lakara", ""), c.get("voice", ""), c.get("purusha", ""), 
                          c.get("eka", ""), c.get("dvi", ""), c.get("bahu", "")))

                # 5. Participles
                for p in data.get("participles", []):
                    cursor.execute("""
                        INSERT INTO participles (dhatu_id, upasarga, derivative, pratyaya, base_form, masculine, feminine, neuter)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """, (dhatu_id, p.get("upasarga", ""), p.get("derivative", ""), p.get("pratyaya", ""), 
                          p.get("base_form", ""), p.get("masculine", ""), p.get("feminine", ""), p.get("neuter", "")))

                # 6. Prayoga
                for pr in data.get("prayoga", []):
                    cursor.execute("""
                        INSERT INTO prayoga (dhatu_id, form, lakara, purusha, vacana, book, literature_text)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (dhatu_id, pr.get("form", ""), pr.get("lakara", ""), pr.get("purusha", ""), 
                          pr.get("vacana", ""), pr.get("book", ""), pr.get("literature_text", "")))
                    
    conn.commit()
    print("Database compiled successfully!")

def build_database_if_missing():
    """Checks for DB and builds it from the packaged JSONs if missing."""
    if os.path.exists(DB_PATH):
        # Database already exists, skip compiling
        return
        
    os.makedirs(APP_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    try:
        create_schema(conn.cursor())
        populate_database(conn)
    except Exception as e:
        print(f"Error compiling database: {e}")
        conn.close()
        # Clean up the broken DB so it tries again next time
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
        raise e
    finally:
        conn.close()

# If you want to test this script directly without importing the package, 
# you can uncomment the next line and run `python db_builder.py`
# build_database_if_missing()