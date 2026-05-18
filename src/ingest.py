from _pytest.nodes import File
from pathlib import Path
import pandas as pd

def load_data(path: str = "data/raw/phiusiil.csv") -> pd.DataFrame:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError(f"Dataset is empty")

    return df


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    return df


def main() -> None:
    df = load_data()
    df = basic_clean(df)

    print("Dataset loaded successfully")
    print(f"Shape: {df.shape}")
    print("Columns: ")
    print(df.columns.tolist())

if __name__ == "__main__":
    main()
    

    