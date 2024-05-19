import sqlite3

def init_db():
    conn = sqlite3.connect('ai_scores.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            demographic_parity REAL,
            equal_opportunity REAL,
            disparate_impact REAL,
            documentation_practices REAL,
            auditability REAL,
            ethical_compliance REAL,
            explainability REAL,
            ui_design REAL,
            decision_doc REAL,
            graph_html TEXT
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
