from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

def load_split_data():
    data_dir = Path("data/processed")

    x_train = pd.read_csv(data_dir/"X_train.csv") # training features
    x_test = pd.read_csv(data_dir/"X_test.csv")   # testing features
    y_train = pd.read_csv(data_dir/"y_train.csv").squeeze() # training lables
    y_test = pd.read_csv(data_dir/"y_test.csv").squeeze()   # testing lables

    return x_train, x_test, y_train, y_test

def keep_numeric(x_train, x_test):
    x_train = x_train.select_dtypes(include = ["number"])
    x_test = x_test.select_dtypes(include = ["number"])

    return x_train, x_test

def scale_data(x_train, x_test):
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)
    return x_train, x_test

def train_model(x_train, y_train): # training the model by using a logisitic regression model
    model = LogisticRegression(max_iter = 2000) # this allows the model to try 2000 times to find a good solution
    model.fit(x_train, y_train) # this allows the model to learn from the data
    return model

def evaluate_model(model, x_test, y_test): # evaluating the model and checks how well the training model did
    y_pred = model.predict(x_test) # the guesses are stored in the y_pred variable

    print(f"Accuracy: {accuracy_score(y_test, y_pred)}") # checks how often the model guessed correctly
    print(f"Classification Report: {classification_report(y_test, y_pred)}") # checks how well the model is able to classify the data


def main():
    x_train, x_test, y_train, y_test = load_split_data()
    x_train, x_test = keep_numeric(x_train, x_test)
    x_train, x_test = scale_data(x_train, x_test)
    model = train_model(x_train, y_train)
    evaluate_model(model, x_test, y_test)

if __name__ == "__main__":
    main()