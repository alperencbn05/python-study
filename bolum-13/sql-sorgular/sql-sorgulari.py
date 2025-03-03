import sqlite3


connection = sqlite3.connect("chinook.db")

cursor = connection.cursor()

sql = "INSERT INTO genres(name) VALUES('Macera')"
cursor.execute(sql)

connection.commit()



connection.close()

# cursor.execute("select * from customers")
# customers = cursor.fetchall()

# for customer in customers:
#     print(customer[0])



