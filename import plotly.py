import plotly.graph_objs as go
import plotly.io as pio

def create_radial_graph(scores, categories, title):
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=scores + [scores[0]],  # Close the loop for the radar chart
        theta=categories + [categories[0]],  # Close the loop for the radar chart
        fill='toself'
    ))

    fig.update_layout(
        title=title,
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]  # Assuming the maximum score is 5
            )),
        showlegend=False
    )

    return pio.to_html(fig, full_html=False)

def main():
    try:
        # Ask for the AI system being evaluated
        title = input("For which AI system are you evaluating? ")

        # Input scores from user
        categories = [
            'Demographic Parity', 'Equal Opportunity', 'Absence of Disparate Impact',
            'Documentation Practices', 'Auditability', 'Compliance with Ethical Guidelines',
            'Explainability', 'User Interface Design', 'Decision-making Documentation'
        ]

        scores = []

        # Fairness Questions
        print("\nFairness Assessment")
        demographic_parity = float(input("Score for Demographic Parity (0-5): "))
        equal_opportunity = float(input("Score for Equal Opportunity (0-5): "))
        disparate_impact = float(input("Score for Absence of Disparate Impact (0-5): "))
        
        scores.extend([demographic_parity, equal_opportunity, disparate_impact])

        # Accountability Questions
        print("\nAccountability Assessment")
        documentation_practices = float(input("Score for Documentation Practices (0-5): "))
        auditability = float(input("Score for Auditability (0-5): "))
        ethical_compliance = float(input("Score for Compliance with Ethical Guidelines (0-5): "))
        
        scores.extend([documentation_practices, auditability, ethical_compliance])

        # Transparency Questions
        print("\nTransparency Assessment")
        explainability = float(input("Score for Explainability (0-5): "))
        ui_design = float(input("Score for User Interface Design (0-5): "))
        decision_doc = float(input("Score for Decision-making Documentation (0-5): "))
        
        scores.extend([explainability, ui_design, decision_doc])

        # Validate scores
        for score in scores:
            if score < 0 or score > 5:
                print("Scores must be between 0 and 5.")
                return

        # Generate the graph HTML
        graph_html = create_radial_graph(scores, categories, title)

        # Save the graph to an HTML file
        with open('radial_graph.html', 'w') as file:
            file.write(graph_html)

        print(f"Radial graph for '{title}' has been saved to 'radial_graph.html'. Open this file in a web browser to view the graph.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == '__main__':
    main()
