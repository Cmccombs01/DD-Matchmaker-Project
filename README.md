🎲 D&D AI Matchmaker Engine
A custom recommendation engine utilizing SQL and AI to optimize user pairing based on complex behavioral, playstyle, and scheduling data.

Engineering Highlights:

Recommendation Algorithms: Engineered a matchmaking logic system to parse unstructured user preferences and pair them with highly compatible groups.

Database Management: Utilized SQL to structure, query, and maintain relational databases of user metrics and availability.

Tech Stack: Python, SQL, AI/LLM Integration, Relational Database Design.
## 🚀 The "Unicorn" Tech Stack
* **Frontend:** Streamlit (Interactive Web Dashboard)
* **Backend:** Python 3.x & Pandas
* **Database:** SQLite3 (Relational structure with 10,000+ records)
* **Data Pipeline:** Automated ETL for CSV, TSV, and Excel (XLSX) formats.
* **AI:** Context-Injected Prompt Engineering for Hallucination-Free Storytelling.

## 📈 Big Data Integration (Kaggle)
This app doesn't just use sample data; it ingests five massive professional datasets:
1.  **7,900+** Premade Characters (TSV)
2.  **600+** World Locations from Faerûn (Excel)
3.  **500+** Spells & Equipment (CSV)
4.  **300+** Monsters with Challenge Ratings (CSV)

## 🧠 Key Engineering Features
* **The ETL Pipeline (`ingest.py`):** A custom script that handles schema normalization, resolving mismatched column headers and hidden white-space errors from multiple data sources.
* **Bulletproof SQL Queries:** Uses dynamic column-finding logic to ensure stability even when external data headers change.
* **AI Context Injection:** A "Premium" feature that pulls random facts (Hero, Location, Monster) from the database to generate 100% lore-accurate adventure hooks.
* **Data Cleaning:** Automated outlier capping and string normalization to maintain database integrity.

## 📂 How to Run
1.  Install requirements: `pip install streamlit pandas openpyxl`
2.  Run `python ingest.py` to build the Big Data vault.
3.  Launch the app: `streamlit run app.py`



