import sqlite3

def run_project():
    connection = sqlite3.connect('dnd_matchmaker.db')
    cursor = connection.cursor()

    # 1. Create Tables
    cursor.execute('CREATE TABLE IF NOT EXISTS players (player_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, playstyle_score INTEGER, is_dm BOOLEAN)')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS adventures (
        adv_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        min_style_score INTEGER,
        max_style_score INTEGER,
        hook TEXT
    )''')
    
    # 2. Add Data
    test_players = [('Grog', 2, 0), ('Jester', 9, 0), ('Matt the DM', 5, 1), ('Brennan the DM', 2, 1)]
    cursor.executemany('INSERT OR IGNORE INTO players (name, playstyle_score, is_dm) VALUES (?, ?, ?)', test_players)

    test_adventures = [
        ('The Red Pit', 1, 4, 'A gladiatorial arena run by a corrupt demon.'),
        ('The Whispering Masquerade', 7, 10, 'A political mystery at a royal ball.'),
        ('The Lost Outpost', 4, 7, 'A mix of exploration and skirmishes in the mountains.')
    ]
    
    # FIXED: Only 4 question marks to match the 4 columns
    cursor.executemany('INSERT OR IGNORE INTO adventures (title, min_style_score, max_style_score, hook) VALUES (?, ?, ?, ?)', test_adventures)

    connection.commit()
    connection.close()

def generate_ultimate_prompt():
    connection = sqlite3.connect('dnd_matchmaker.db')
    cursor = connection.cursor()

    query = """
    SELECT 
        p.name, dm.name, adv.title, adv.hook
    FROM players p
    JOIN players dm ON p.is_dm = 0 AND dm.is_dm = 1
    JOIN adventures adv ON p.playstyle_score BETWEEN adv.min_style_score AND adv.max_style_score
    WHERE ABS(p.playstyle_score - dm.playstyle_score) <= 2
    LIMIT 1;
    """
    
    cursor.execute(query)
    match = cursor.fetchone()

    if match:
        p_name, dm_name, adv_title, adv_hook = match
        
        ai_prompt = f"""
        ACT AS A PROFESSIONAL NARRATIVE DESIGNER.
        - Match: Player [{p_name}] and DM [{dm_name}].
        - Adventure: "{adv_title}"
        - Hook: "{adv_hook}"
        
        TASK: Write a short intro for this campaign.
        """
        print("\n--- 🐉 ULTIMATE CAMPAIGN PROMPT ---")
        print(ai_prompt)
    else:
        print("\nNo perfect match found today. Try adding more adventures!")

    connection.close()

if __name__ == "__main__":
    run_project()
    generate_ultimate_prompt()