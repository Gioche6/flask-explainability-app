from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import plotly.graph_objs as go
import plotly.io as pio
import os

app = Flask(__name__)

def init_db():
    with sqlite3.connect('ai_scores.db') as conn:
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get input values from the form
        title = request.form['title']

        # Fairness
        demographic_parity = float(request.form['demographic_parity'])
        equal_opportunity = float(request.form['equal_opportunity'])
        disparate_impact = float(request.form['disparate_impact'])

        # Accountability
        documentation_practices = float(request.form['documentation_practices'])
        auditability = float(request.form['auditability'])
        ethical_compliance = float(request.form['ethical_compliance'])

        # Transparency
        explainability = float(request.form['explainability'])
        ui_design = float(request.form['ui_design'])
        decision_doc = float(request.form['decision_doc'])

        # Create the radial graph
        categories = [
            'Demographic Parity', 'Equal Opportunity', 'Absence of Disparate Impact',
            'Documentation Practices', 'Auditability', 'Compliance with Ethical Guidelines',
            'Explainability', 'User Interface Design', 'Decision-making Documentation'
        ]
        scores = [
            demographic_parity, equal_opportunity, disparate_impact,
            documentation_practices, auditability, ethical_compliance,
            explainability, ui_design, decision_doc
        ]

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=scores + [scores[0]],  # Close the loop for the radar chart
            theta=categories + [categories[0]],  # Close the loop for the radar chart
            fill='toself',
            line=dict(color='blue'),
        ))

        fig.update_layout(
            title=title,
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5]  # Assuming the maximum score is 5
                )),
            showlegend=False,
            template="plotly_dark"  # Change the template for a different style
        )

        # Save the figure as an HTML div string
        graph_html = pio.to_html(fig, full_html=False)

        # Save data to the database
        with sqlite3.connect('ai_scores.db') as conn:
            c = conn.cursor()
            c.execute('''
                INSERT INTO scores (
                    title, demographic_parity, equal_opportunity, disparate_impact,
                    documentation_practices, auditability, ethical_compliance,
                    explainability, ui_design, decision_doc, graph_html
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                title, demographic_parity, equal_opportunity, disparate_impact,
                documentation_practices, auditability, ethical_compliance,
                explainability, ui_design, decision_doc, graph_html
            ))
            conn.commit()

        return redirect(url_for('results'))

    except ValueError:
        return "Invalid input. Please enter numeric values."

@app.route('/results')
def results():
    with sqlite3.connect('ai_scores.db') as conn:
        c = conn.cursor()
        c.execute('SELECT id, title, graph_html FROM scores')
        rows = c.fetchall()
    return render_template('results.html', rows=rows)

@app.route('/view/<int:id>')
def view(id):
    with sqlite3.connect('ai_scores.db') as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM scores WHERE id = ?', (id,))
        row = c.fetchone()
    return render_template('view.html', row=row)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
