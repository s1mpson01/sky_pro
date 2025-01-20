import pandas as pd


def get_transactions_from_excel(path: str) -> list:
    """
    Cчитывает финансовые операций из excel-файла
    """
    try:
        df = pd.read_excel(f"{path}")
        result = df.to_dict(orient="records")
    except Exception:
        raise Exception("Excel файл не найден")
    else:
        return result


def get_transactions_from_csv(path: str) -> list:
    """
    Cчитывает финансовые операций из CSV-файла
    """
    try:
        df = pd.read_csv(f"{path}", sep=";")
        result = df.to_dict(orient="records")
    except Exception:
        raise Exception("Csv файл не найден")
    else:
        return result
