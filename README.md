# Banking operations

Наш проект направлен на облегчение задач банка и на использование виджетов клиентом.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш_репозиторий.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd ваш_проект
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Использование

Примеры использования простых функций:

```python
from src.processing import filter_by_state, sort_by_date

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)
```

Примеры использований генераторов в функциях:
```python
from src.generators import transaction_descriptions
from tests.conftest import transactions

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

# >>> Перевод организации
#     Перевод со счета на счет
#     Перевод со счета на счет
#     Перевод с карты на карту
#     Перевод организации
```

Примеры использований декоратора:

```python
from src.decorators import log


@log(filename='')
def my_function(x, y):
   return x + y


my_function(1, 2)

# >>> my_function ok
```

## Тестирование

В нашем проекте используется тестирование для корректности работы. Мы использовали фреймвор pytest.
Все написанные тесты находятся в папке tests, там же лежит файл со всеми фикстурами и параметризациями (модуль "conftest.py")

```
File	        statements missing excluded coverage
src\__init__.py	     0	     0	     0	     100%
src\decorators.py   20       3       0        85%
src\external_api.py 17	     0	     0	     100%
src\generators.py    9	     0	     0	     100%
src\masks.py	    17	     0	     0	     100%
src\processing.py    8	     0	     0	     100%
src\utils.py	    13	     2	     0	      85%
src\widget.py	    24	     0	     0	     100%
Total	            58	     0	     0	     100%
```