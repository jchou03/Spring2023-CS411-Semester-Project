


import mysql.connector

db = mysql.connector.connect(user='root', host='127.0.0.1', port=3306, password='Hikeleftstation12', database='space_missions')

cursor = db.cursor()

query = ('''select s.spaceship_name, d.destination_name, m.description from spaceships s, destinations d, missions m where s.sid = m.sid AND d.did = m.did;''')

cursor.execute(query)

for info in cursor: print(info)

cursor.close()

db.close()
