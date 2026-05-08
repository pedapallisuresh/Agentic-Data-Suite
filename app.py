import pandas as pd
from agents.analyst import AnalystAgent
from agents.cleaner import CleanerAgent
from agents.researcher import ResearcherAgent

def main():
    # Load data
    data = pd.read_csv('data/sample.csv')
    print("Data loaded successfully.")

    # Clean data
    cleaner = CleanerAgent()
    cleaned_data = cleaner.clean(data)
    print("Data cleaned.")

    # Analyze data
    analyst = AnalystAgent()
    insights = analyst.analyze(cleaned_data)
    print("Analysis completed:", insights)

    # Research
    researcher = ResearcherAgent()
    research_results = researcher.research(insights)
    print("Research completed:", research_results)

if __name__ == "__main__":
    main()