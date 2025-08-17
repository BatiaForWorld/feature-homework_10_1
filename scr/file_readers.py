import csv

import pandas as pd


def read_transactions_from_csv(file_path: str) -> list:
    """
    Функция считывает финансовые операции из CSV файла.
    """
    try:
        transactions = []
        with open(file_path, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transactions.append(dict(row))

        return transactions

    except FileNotFoundError:
        return []
    except csv.Error:
        return []
    except Exception:
        return []


def read_transactions_from_excel(file_path: str) -> list:
    """
    Функция считывает финансовые операции из Excel файла.
    """
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict("records")

        return transactions

    except FileNotFoundError:
        return []
    except pd.errors.EmptyDataError:
        return []
    except Exception:
        return []
