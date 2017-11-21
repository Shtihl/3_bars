# Ближайшие бары

Скрипт для определения самого большого бара, самого маленького и самого ближайшего к заданным координатам. Поиск происходит на основе данных с [data.mos.ru](http://data.mos.ru).
Для получения данных в формате JSON:

1. Зарегистрироваться, получить ключ API
2. Скачать файл по ссылке вида ```https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}```

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py path_to_json_file_with_data # possibly requires call of python3 executive instead of just python
The biggest Bar: Спорт бар «Красная машина»
Number of seats: 450

The smallest Bar: Сушистор
Number of seats: 0

To find the nearest bar, enter your coordinates
Enter your latitude 55.699058
Enter your longitude 37.917861

Nearest bar: Таверна
Address: проспект Защитников Москвы, дом 8

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)