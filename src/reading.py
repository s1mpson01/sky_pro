import pandas as pd


def get_transactions_from_excel(path):
    df = pd.read_excel(f"{path}")
    result = df.to_dict(orient="records")
    return result


def get_transactions_from_csv(path):
    df = pd.read_csv(f"{path}", sep=";")
    result = df.to_dict(orient="records")
    return result
