"""
Модуль реализует пользовательский интерфейс, загрузку данных из файлов и вызовы логики.
"""

import json
import os

import pandas as pd

from scr.logic import (
    filter_by_status,
    filter_rub_transactions,
    format_transaction,
    process_bank_search,
    sort_transactions_by_date,
)

AVAILABLE_STATUSES = ["EXECUTED", "CANCELED", "PENDING"]
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


def read_transactions_from_csv(csv_path: str) -> list:
    try:
        df = pd.read_csv(csv_path, delimiter=";")
        return df.to_dict(orient="records")
    except Exception:
        print(f"Ошибка чтения CSV-файла: {csv_path}")
        return []


def read_transactions_from_excel(xlsx_path: str) -> list:
    try:
        df = pd.read_excel(xlsx_path)
        return df.to_dict(orient="records")
    except Exception:
        print(f"Ошибка чтения XLSX-файла: {xlsx_path}")
        return []


def load_transactions(json_path: str) -> list:
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return [item for item in data if isinstance(item, dict)]
            else:
                print(f"Файл {json_path} не содержит список. Тип данных: {type(data)}")
                return []
    except Exception as e:
        print(f"Ошибка при загрузке файла {json_path}: {str(e)}")
        return []


def main():
    """
    Основная функция программы. Запускает меню, обрабатывает выбор пользователя,
    загружает данные из выбранного файла и вызывает соответствующие функции логики.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    choice = input("Пользователь: ").strip()

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        json_path = os.path.join(DATA_DIR, "operations.json")
        try:
            transactions = load_transactions(json_path)
        except Exception:
            print("Ошибка чтения JSON-файла.")
            return
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        csv_path = os.path.join(DATA_DIR, "transactions.csv")
        try:
            transactions = read_transactions_from_csv(csv_path)
        except Exception:
            print("Ошибка чтения CSV-файла.")
            return
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        xlsx_path = os.path.join(DATA_DIR, "transactions_excel.xlsx")
        try:
            transactions = read_transactions_from_excel(xlsx_path)
        except Exception:
            print("Ошибка чтения XLSX-файла.")
            return
    else:
        print("Некорректный выбор. Завершение работы.")
        return

    """Фильтрация по статусу с повторным запросом"""
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные для фильтровки статусы: {', '.join(AVAILABLE_STATUSES)}")
        status = input("Пользователь: ").strip()
        filtered = filter_by_status(transactions, status)
        if filtered:
            print(f'Операции отфильтрованы по статусу "{status.upper()}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    """Сортировка по дате с повторным запросом"""
    while True:
        print("Отсортировать операции по дате? Да/Нет")
        sort_ans = input("Пользователь: ").strip().lower()
        if sort_ans in ["да", "нет"]:
            break
        else:
            print("Пожалуйста, введите 'Да' или 'Нет'.")
    if sort_ans == "да":
        while True:
            print("Отсортировать по возрастанию или по убыванию?")
            order = input("Пользователь: ").strip().lower()
            if order in ["по возрастанию", "по убыванию"]:
                reverse = order == "по убыванию"
                filtered = sort_transactions_by_date(filtered, reverse=reverse)
                break
            else:
                print("Пожалуйста, введите 'по возрастанию' или 'по убыванию'.")

    """ Фильтрация по рублям с повторным запросом"""
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        rub_ans = input("Пользователь: ").strip().lower()
        if rub_ans in ["да", "нет"]:
            break
        else:
            print("Пожалуйста, введите 'Да' или 'Нет'.")
    if rub_ans == "да":
        filtered = filter_rub_transactions(filtered)

    """ Поиск по описанию с повторным запросом"""
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        desc_ans = input("Пользователь: ").strip().lower()
        if desc_ans in ["да", "нет"]:
            break
        else:
            print("Пожалуйста, введите 'Да' или 'Нет'.")
    if desc_ans == "да":
        search = input("Введите слово или паттерн для поиска: ").strip()
        if search:
            filtered = process_bank_search(filtered, search)

    print("Распечатываю итоговый список транзакций...")
    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered)}")
        for t in filtered:
            print()
            print(format_transaction(t))


if __name__ == "__main__":
    main()
