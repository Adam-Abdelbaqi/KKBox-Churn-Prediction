import pandas as pd
from pathlib import Path


def load_data(filepath: str)-> pd.DataFrame:
    """
    Loads Expresso Telecom Churn Dataset
    """
    project_root = Path(__file__).parents[2]
    Data_Path = project_root / filepath
    
    try:
        df = pd.read_csv(Data_Path)

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Dataset Is Not Found At {Data_Path}") from e

    return df