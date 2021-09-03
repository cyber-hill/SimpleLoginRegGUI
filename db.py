# -*- coding: utf-8 -*-
import sqlite3,hashlib
conn = sqlite3.connect("main.db",check_same_thread=False)
cursor = conn.cursor()
def adduser(fullname,username,password):
    hash_object = hashlib.sha256(password.encode('utf-8'))
    password_hash = hash_object.hexdigest()
    user = (f'{fullname}',f'{username}',f'{password_hash}')
    cursor.execute("INSERT INTO users VALUES(?, ?, ?);", user)
    conn.commit()


