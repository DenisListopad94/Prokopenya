import sqlite3

con = sqlite3.connect("homework2sql.db")
cur = con.cursor()

# 1. Подключить готовую базу с актёрами и режиссёрами использую SQLite3.
# При помощи “сырого” запроса вывести все фильмы, которые были сняты с 2015 по 2020 год.

res = cur.execute("SELECT name_movie FROM movies where release between 2015 and 2020")
print(res.fetchall())


# 4. Использую SQLite3 при помощи “сырого”  запроса вывести первых 5 самых высокооплачиваемых актёров.

res = cur.execute("SELECT name, surname FROM actors, bank_accounts ORDER BY finance DESC LIMIT 5;")
for actor in res:
    print(actor)


con.close()

