# CHAT-SOL

CHAT-SOL is a Streamlit-based web application that allows you to chat with your SQL database using natural language, powered by LangChain and LLMs.

## Features

- Chat with your local SQLite (`student.db`) or connect to your own MySQL database.
- Uses LangChain's SQL agent to translate natural language queries into SQL.
- Supports Llama3-8b-8192 via the GROQ API for intelligent query generation.
- Interactive chat interface with message history.

## Getting Started

### Prerequisites

- Python 3.8+
- [GROQ API Key](https://console.groq.com/)

### Installation

1. Clone this repository.
2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. (Optional) Set up your `.env` file for environment variables.

### Usage

1. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

2. Open the app in your browser (usually at `http://localhost:8501`).

3. Choose your database:
    - **SQLite**: Uses the included `student.db` file.
    - **MySQL**: Enter your MySQL connection details.

4. Enter your GROQ API key in the sidebar.

5. Start chatting with your database!

## Database

- The default `student.db` SQLite database is created by running [`sqlite.py`](sqlite.py).
- It contains a `STUDENT` table with sample records.

## File Structure

- `app.py` - Main Streamlit application.
- `sqlite.py` - Script to create and populate the SQLite database.
- `student.db` - Sample SQLite database.
- `requirements.txt` - Python dependencies.
- `.env` - (Optional) Environment variables.
- `README.md` - Project documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file