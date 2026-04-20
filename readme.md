# Agentic Data Suite

Agentic Data Suite is a modular Python project designed for data analysis, cleaning, and research workflows. It leverages an agent-based architecture to separate concerns and streamline data-driven tasks.

## Project Structure

```
agentic-data-suite/
│
├── app.py                  # Main application entry point
├── requirements.txt        # Python dependencies
├── agents/                 # Agent modules
│   ├── __init__.py
│   ├── analyst.py          # Analyst agent logic
│   ├── cleaner.py          # Data cleaning agent logic
│   └── researcher.py       # Research agent logic
├── data/
│   └── sample.csv          # Example data file
└── .streamlit/
    └── secrets.toml        # (Optional) Streamlit secrets/config
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd agentic-data-suite
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare your data:**
   - Place your CSV or other data files in the `data/` directory.

2. **Run the application:**
   ```bash
   python app.py
   ```
   - The main script will orchestrate the agents for analysis, cleaning, and research tasks.

3. **Configure secrets (optional):**
   - If using Streamlit or external APIs, add credentials to `.streamlit/secrets.toml`.

## Agents Overview

- **Analyst Agent (`agents/analyst.py`):**
  - Performs data analysis, generates insights, and summarizes findings.
- **Cleaner Agent (`agents/cleaner.py`):**
  - Handles data cleaning, preprocessing, and validation.
- **Researcher Agent (`agents/researcher.py`):**
  - Conducts research tasks, such as literature review or data enrichment.

Each agent is implemented as a separate Python module for modularity and ease of extension.

## Customization

- Add new agents by creating Python files in the `agents/` directory and updating `app.py` to use them.
- Replace `sample.csv` with your own datasets.

## Example Workflow

1. **Data Loading:** The main app loads data from `data/sample.csv`.
2. **Cleaning:** The Cleaner agent processes and cleans the data.
3. **Analysis:** The Analyst agent analyzes the cleaned data and produces summaries.
4. **Research:** The Researcher agent augments the analysis with external research or enrichment.
5. **Results:** Outputs are displayed or saved as needed.

## Requirements

- Python 3.8+
- See `requirements.txt` for required packages.

## License

MIT License (or specify your license here)

---

**Feel free to extend this project with new agents or integrate with other tools!**
