# Проект Home work of Kazantsev Company

## Описание:

Проект Home work of Kazantsev Company - это приложение на Python для проверки наставникам.

## Установка:

1. Клонируйте репозиторий:

```
git clone https://github.com/BatiaForWorld/feature-homework_10_1.git
```

2. Зависимости в файле ```pyproject.toml```
3. ## Использование:

1. Откройте приложение PyCharm.
2. Клонирйте проект
3. Проект оснащён тестами. Исользуйте команду pytest для тестирования:

```
poetry run pytest --cov
```
4. Для проверки модуля generators.py создайте файл с любым названием
   в директории проекта и скопируйте в него данный код:

```
from scr.generators import card_number_generator, filter_by_currency, transaction_descriptions

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

filter = filter_by_currency(transactions, "USD")
print(next(filter))
print(next(filter))

card_number = card_number_generator(1, 5)
print(next(card_number))
print(next(card_number))
print(next(card_number))
print(next(card_number))

descriptions = transaction_descriptions(transactions)
print(next(descriptions))
print(next(descriptions))
print(next(descriptions))
print(next(descriptions))
print(next(descriptions))

```

5. Файл ****decorators.py**** содержит декоратор ***log***, 
который будет автоматически регистрировать детали выполнения функций,
такие как время вызова, имя функции, передаваемые аргументы, 
результат выполнения и информация об ошибках.
  Это позволит обеспечить более глубокий контроль 
и анализ поведения программы в процессе ее выполнения.

  Для проверки модуля decorators.py добавьте код в конце файла:

```
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

```
Ожидаемый вывод в лог-файл mylog.txt
при успешном выполнении:

```my_function ok```

Ожидаемый вывод при ошибке:

```my_function error: тип ошибки. Inputs: (1, 2), {}```
Где тип ошибки заменяется на текст ошибки.

6. Модуль utils.py содержит функцию, которая принимает на вход путь до JSON-файла
и возвращает список словарей с данными о финансовых транзакциях. 
Если файл пустой, содержит не список или не найден, функция возвращает пустой список. 

    Файл с данными о финансовых транзациях operations.json 
лежит в директории data/ в корне проекта.
  
Для проверки работы функции ***utils.py*** добавьте в конце файла:

```
operations = load_transactions("../data/operations.json")
print(f"Загружено операций: {len(operations)}")
```

7. Модуль external_api.py реализует функцию, 
которая принимает на вход транзакцию и возвращает сумму транзакции
 (amount) в рублях, тип данных — float. Если транзакция была в USD или EUR,
происходит обращение к внешнему API для получения текущего курса валют 
и конвертации суммы операции в рубли. 
Для конвертации валюты воспользуйтесь Exchange Rates Data API:
https://apilayer.com/exchangerates_data-api. 

Используйте переменные окружения из файла .env для сокрытия чувствительных
данных (токенов доступа для API). Файла .env и размещён в репозитории данного проекта
на GitHub


## Документация:

Для получения дополнительной информации обратитесь к [документации](README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT RF](LICENSE).
