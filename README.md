# Проект на python

## Описание:

Это проект на бэкенде будет готовить данные 
для отображения в новом виджете.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/s1mpson01/sky_pro.git
```
2. Установка окружения:
```
pip install poetry
poetry init
```
## Тестирование проекта
* Наш проект покрыт тестами фреймворка Pytest.
* Установка. ` pip install pytest`
* Отчет .......


## Использование
Генератор который генерирует 
номера банковских карт в формате 
XXXX XXXX XXXX XXXX. Где 1 и 5 границы диапазонов
```
for card_number in card_number_generator(1, 5):
    print(card_number)
```
## Прочая информация
1. Добавлен модуль generators.py
2. Добавлен модуль decorators.py 
который логирует результат работ в файл 
3. Добавлен модуль reading для чтения данных 
из excel и csv файлов
4. Добавлен модуль searching для поиска информации по критериям
5. Добавлен модуль main который связывает все зависимости проекта