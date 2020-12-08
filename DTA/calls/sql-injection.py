import sys
import os
import sqlite3

def makeTainted(tainted_var):
    return ""

def makeCondTainted(tainted_var, taint_cond1):
    return ""

def makeCondTainted(tainted_var, taint_cond1, taint_cond2):
    return ""

def isTainted(tainted_var):
    return True

def is_sqli(tainted_var):
    return True

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
makeTainted(user_id)


print("Insert your password")
password = input()
makeTainted(password)


retrieve_user = "SELECT * FROM credentials WHERE user_id = '" + user_id + "' and password = '" + password + "';"
makeCondTainted(retrieve_user, user_id, password)

if isTainted(retrieve_user) and is_sqli(retrieve_user):
    print("Sql Injection")
    exit(-1)

cursor = conn.execute(retrieve_user)
makeCondTainted(cursor, retrieve_user)


entries = cursor.fetchall()
makeCondTainted(entries, cursor)

if len(entries) > 0:
    print("\n===Logged-in=====")
    retrieve_user = "SELECT * FROM accounts WHERE user_id = '" + user_id + "';"
    makeCondTainted(retrieve_user, user_id, password)

    if isTainted(retrieve_user) and is_sqli(retrieve_user):
        print("Sql Injection")
        exit(-1)

    cursor = conn.execute(retrieve_user)
    makeCondTainted(cursor, retrieve_user)

    entries = cursor.fetchall()
    makeCondTainted(entries, cursor)

    for entry in entries:
        makeCondTainted(entry, entries)

        user_id, first_name, last_name, phone = entry
        makeCondTainted(user_id, entry)
        makeCondTainted(first_name, entry)
        makeCondTainted(last_name, entry)
        makeCondTainted(phone, entry)

        if isTainted(user_id) or isTainted(first_name) or isTainted(last_name) or isTainted(phone):
            print("Printing Tainted Values")
            exit(-1)

        print()
        print("Here is {} data:".format(user_id))
        print("user-id=", user_id)
        print("first_name=", first_name)
        print("last_name=", last_name)
        print("phone", phone)
else:
    print("Wrong credentials")