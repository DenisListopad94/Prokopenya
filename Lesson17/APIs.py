# Используя один из предложенных API, или свой API, получить информацию о данном API (https://restcountries.com/)
# Используя requests вывести информацию об каком-то одном instance.
# Получить данные из API, отсортировав их по какому-либо признаку. Например, если вы используете API для получения
# новостей покажите только новости определенной категории или из определенного источника.
# Проанализируйте ваше API. Например: извлеките определенные данные из ответа ( получите заголовки новостей из
# JSON-ответа и вывести их на экран).

# 1.Используя requests вывести информацию об каком-то одном instance.

import requests
from restcountries import RestCountryApiV2 as rapi


def info_about_country(country_name):
    country_list = rapi.get_countries_by_name(country_name)
    country = country_list[0]
    print(f'Столица Республики Беларусь {country.capital},\nЯзык {country.languages[0]['name']}, '
          f'{country.languages[1]['name']}')


info_about_country("Belarus")

# 2. # Получить данные из API, отсортировав их по какому-либо признаку. Например, если вы используете API для получения
# # новостей покажите только новости определенной категории или из определенного источника.


def get_all_countries():
    country_list = rapi.get_all()
    for data in country_list:
        print(f'Страна - {data},\nНасление - {data.population}')


get_all_countries()

# 3. Проанализируйте ваше API. Например: извлеките определенные данные из ответа ( получите заголовки новостей из
# JSON-ответа и вывести их на экран).


def json_info():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)

    if response.status_code == 200:
        countries = response.json()
        for country in countries:
            print(f'Страна - {country['name']['common']}: столица - {country['capital']}')
    else:
        print("Ошибка при получении данных:", response.status_code)


json_info()



