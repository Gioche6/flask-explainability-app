# Explainability Scoring System

This project is a web application that evaluates AI systems based on various criteria such as fairness, accountability, and transparency. The scores are visualized using a radial graph, and the data is stored in an SQLite database.

## Features

- **Fairness Assessment**: Evaluates AI systems based on demographic parity, equal opportunity, and absence of disparate impact.
- **Accountability Assessment**: Scores AI systems on documentation practices, auditability, and compliance with ethical guidelines.
- **Transparency Assessment**: Measures explainability, user interface design, and decision-making documentation.
- **Data Storage**: Stores the assessment scores and generated graphs in an SQLite database.
- **Graph Visualization**: Displays a radial graph representing the scores.

## Technologies Used

- **Python**: Programming language used for the backend.
- **Flask**: Micro web framework for Python.
- **SQLite**: Database for storing scores and graphs.
- **Plotly**: Library for creating interactive graphs.
- **Bootstrap**: Frontend framework for styling the web pages.
- **Heroku**: Platform for deploying the web application.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/explainability-scoring-system.git
    cd explainability-scoring-system
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Initialize the database:**
    ```bash
    python database_setup.py
    ```

5. **Run the application:**
    ```bash
    python app.py
    ```

6. **Open your browser and visit:**
    ```
    http://127.0.0.1:5000
    ```

## Deployment

To deploy the application on Heroku, follow these steps:

1. **Login to Heroku:**
    ```bash
    heroku login
    ```

2. **Create a new Heroku app:**
    ```bash
    heroku create your-app-name
    ```

3. **Push the code to Heroku:**
    ```bash
    git push heroku main
    ```

4. **Run database setup on Heroku:**
    ```bash
    heroku run python database_setup.py
    ```

5. **Open the deployed app:**
    ```bash
    heroku open
    ```

## Usage

1. **Home Page**: Enter the AI system title and scores for each criterion, then click "Calculate".
2. **View Results**: Click "View Stored Scores" to see all stored scores and view individual score details and graphs.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com).

