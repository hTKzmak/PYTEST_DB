import sqlite3
coding: 'utf-8'

connection = sqlite3.connect('../mainDB.db')
cursor = connection.cursor()


# # Таблица/БД с собаками
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Dogs (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# breed TEXT NOT NULL,
# age INTEGER
# )
# ''')


# # Таблица/БД с питомниками
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Nursery (
# id INTEGER PRIMARY KEY,
# city TEXT NOT NULL,
# dogs INTEGER
# )
# ''')


# # Таблица/БД с пользователями
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users (
# id INTEGER PRIMARY KEY,
# FirstName TEXT NOT NULL,
# LastName TEXT NOT NULL,
# PreferredBreeds TEXT
# )
# ''')


# # Выбираем всех пользователей
# cursor.execute('SELECT name, id FROM Dogs WHERE id = ?', (2,))
# dogs = cursor.fetchall()
#
# # Выводим результаты
# for i in dogs:
#     print(i)

# connection.commit()

connection.close()