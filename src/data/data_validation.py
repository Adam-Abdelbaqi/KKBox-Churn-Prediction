import pandas as pd

def validate_data(df:pd.DataFrame , target = "CHURN" , require_target: bool = True)-> None:

    # Validating that the Dataset is not Empty.
    if df.empty:
        raise ValueError("Dataset Cannot Be Empty.")

    # Checking that the Target Variable (CHURN) Exists in the Training Data Only.
    if require_target and target not in df.columns:
        raise KeyError(f"Missing Column {target} Should Be Included.")

    
    