import pandas as pd

def load_data():
    df = pd.read_csv("data/mall_customers_india.csv")

    print("Dataset Loaded Successfully")
    print(df.head())

    return df