from pathlib import Path
from sklearn.model_selection import train_test_split
from ingest import load_data, basic_clean


def split_data():
    df = load_data()
    df = basic_clean(df)

    target_col = "label"

    X = df.drop(columns=[target_col])
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    X_train.to_csv(output_dir / "X_train.csv", index=False)
    X_test.to_csv(output_dir / "X_test.csv", index=False)
    y_train.to_csv(output_dir / "y_train.csv", index=False)
    y_test.to_csv(output_dir / "y_test.csv", index=False)

    print("Split complete")
    print(f"X_train: {X_train.shape}")
    print(f"X_test: {X_test.shape}")


if __name__ == "__main__":
    split_data()