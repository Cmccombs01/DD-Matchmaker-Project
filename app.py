import streamlit as st
import sqlite3
import pandas as pd

# 1. Setup the Webpage Look
st.set_page_config(page_title="D&D Matchmaker Dashboard", page_icon="🐉")
st.title("🐉 D&D Campaign Architect")
st.markdown("---")

# 2. Sidebar for User Input
st.sidebar.header("Matchmaker Settings")
min_score = st.sidebar.slider("Minimum Roleplay Score", 0, 10, 5)
item_type = st.sidebar.selectbox("Lookup Item Type", ["Spell", "Weapon", "Armor"])

# 3. Connect to your 'Brains' (Database)
def get_data(query, params=()):
    conn = sqlite3.connect('dnd_matchmaker.db')
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df

# 4. Display the "Current Players" Table
st.subheader("Current Player Roster")
players_df = get_data("SELECT name, playstyle_score, is_dm FROM players")
st.dataframe(players_df, use_container_width=True)

# 5. Interactive Recommendation Logic
st.subheader(f"Recommended {item_type}s")
recs_query = "SELECT name, playstyle_score FROM players WHERE playstyle_score >= ?"
recs_df = get_data(recs_query, (min_score,))

if not recs_df.empty:
    st.success(f"Found {len(recs_df)} players who might like a {item_type}!")
    st.table(recs_df)
else:
    st.warning("No players match this roleplay threshold.")

st.markdown("---")
st.caption("Built with Python, SQL, and Streamlit | Portfolio Project 2026")