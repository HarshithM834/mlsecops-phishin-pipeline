import json as js
import pandas as pd
from pathlib import Path

def validate_csv(csv_path, schema_path):
    df = pd.read_csv(csv_path)

    with open(schema_path, "r") as file:
        schema = js.load(file) 

    required_columns = schema.get("required", [])

    missing_columns = []
    for col in required_columns:
        if col not in df.columns:
            missing_columns.append(col)

    if len(missing_columns) > 0:
        raise ValueError(f"Missing required columns in DataFrame: {missing_columns}")

    if "label" in df.columns:
        allowed_labels = [0, 1]
        invalid_values = []

        for val in df["label"].unique():
            if val not in allowed_labels:
                invalid_values.append(val)

        if len(invalid_values) > 0:
            raise ValueError(f"Label column contains invalid values: {invalid_values}")
        

    print("Validation Passed")


if __name__ == "__main__":
    validate_csv("data/raw/phiusiil.csv", "schema.json")