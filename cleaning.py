import sqlite3

def clean_and_validate_data():
    print("--- 🧹 STARTING DATA CLEANING PROCESS ---")
    
    # These represent 'Messy' sign-ups from the web
    raw_signups = [
        ("  cleric_girl_99  ", 8, 0),  # Problem: Extra spaces
        ("", 5, 0),                    # Problem: Missing name
        ("BARBARIAN_BOB", 150, 0),     # Problem: Score is too high (Max is 10)
        ("DungeonMaster_Steve", 5, 1)  # Correct entry
    ]

    cleaned_data = []

    for name, score, is_dm in raw_signups:
        # 1. Strip extra spaces
        clean_name = name.strip()
        
        # 2. Validation: Check if name is empty
        if not clean_name:
            print(f"⚠️ SKIPPING: Found an entry with a missing name.")
            continue
            
        # 3. Validation: Cap the score at 10
        if score > 10:
            print(f"🔧 CORRECTING: {clean_name}'s score was {score}. Capping at 10.")
            score = 10
        
        # 4. Formatting: Make names Title Case
        clean_name = clean_name.replace("_", " ").title()
        
        cleaned_data.append((clean_name, score, is_dm))

    # Save the 'Clean' data to the database
    connection = sqlite3.connect('dnd_matchmaker.db')
    cursor = connection.cursor()
    
    cursor.executemany('INSERT OR IGNORE INTO players (name, playstyle_score, is_dm) VALUES (?, ?, ?)', cleaned_data)
    
    connection.commit()
    print(f"✅ CLEANING COMPLETE: Added {len(cleaned_data)} valid players to the database.")
    connection.close()

if __name__ == "__main__":
    clean_and_validate_data()