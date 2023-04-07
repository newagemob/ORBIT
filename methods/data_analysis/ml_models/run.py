from pathlib import Path
import datetime as dt
from methods.data_analysis.ml_models.decision_tree import DecisionTree

def run_machine_readable() -> None:
    """
    This function creates a CSV file of the top 10 companies by market cap in data_visualization/output/sp500_stocks.csv
    """
    project_dir = Path(__file__).resolve().parents[3]
    csv_file = f"{project_dir}/methods/data_collection/output/SP500/yahoo_sp500_stocks_{dt.date.today()}.csv"
    decision_tree = DecisionTree(csv_file)
    model = decision_tree.build_model()
    print(model)


run_machine_readable()
