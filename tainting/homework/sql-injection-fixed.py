import sys
import os
import sqlite3

# Connect to database
conn = None
try:
    conn = sqlite3.connect('users.db')
except Exception:
    print("Can't connect to the database")
    sys.exit(-1)

print("Welcome to this vulnerable database reader")
print("You have to login first")

print("Insert your user-id")
user_id = input()

print("Insert your password")
password = input()

cursor = conn.execute("SELECT * FROM credentials WHERE user_id = ? and password = ?;", (user_id, password))

entries = cursor.fetchall()
if len(entries) > 0:
    print("\n===Logged-in=====")
    cursor = conn.execute("SELECT * FROM accounts WHERE user_id = ?;", user_id)

    entries = cursor.fetchall()
    for entry in entries:
        user_id, first_name, last_name, phone = entry
        print()
        print("Here is {} data:".format(user_id))
        print("user-id=", user_id)
        print("first_name=", first_name)
        print("last_name=", last_name)
        print("phone", phone)
else:
    print("Wrong credentials")