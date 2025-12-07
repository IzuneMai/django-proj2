import sqlite3
con = sqlite3.connect('main.db')
cur = con.cursor()

#таблица пользователей

cur.execute(f'CREATE TABLE users ("id" INTEGER, "username" VARCHAR(30) UNIQUE, "password" VARCHAR(30),"email" VARCHAR(30), PRIMARY KEY("id" AUTOINCREMENT))')

con.commit()