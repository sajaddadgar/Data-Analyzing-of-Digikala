# Import libraries
import mysql.connector
import pandas as pd
import re
import json

# Establish a MySQL connection
mydb = mysql.connector.connect(host="localhost", user="root", password="java123")

# Get cursor, which is used to traverse the database, line by line
cursor = mydb.cursor()

# Create a database
cursor.execute("use mytest2;")

# Create a table for mobile, laptop, tablet, gaming console, headphone, speaker
cursor.execute("create table customers  " 
               "(id int primary key auto_increment,"
               "id_order int,"
               "id_customer int,"
               "id_item int,"
               "dateTime_cartfinalize datetime,"
               "amount_gross_order int,"
               "city_name_fa varchar(30),"
               "quantity_item int);")

info = pd.read_excel("data/3.xlsx")
head = list(info)

col = []
for i in range(head.__len__()):
    col.append(pd.DataFrame(info, columns=[head[i]]))
info_value = []
for i in range(head.__len__()):
    info_value.append(col[i].get_values())


cursor.execute('select * from customers')
data=cursor.fetchall()
# This part check mobile's table is empty or not, if table is'nt empty, no action is needed
if not data:
# Filter mobiles
    for i in range(col[0].__len__()):

        query= """insert into customers (
                    id_order, id_customer, id_item, dateTime_cartfinalize, amount_gross_order, city_name_fa, quantity_item)
                    values (%s, %s, %s, %s, %s, %s, %s)"""
        # insert values of cells without brackets and parantheses and quotation marks
        value=(int(info_value[0][i]),
                int(info_value[1][i]),
                int(info_value[2][i]),
                str(info_value[3][i])[2:len(str(info_value[3][i]))-2],
                int(info_value[4][i]),
                str(info_value[5][i])[2:len(str(info_value[5][i]))-2],
                int(info_value[6][i]))
        # Insert operation
        cursor.execute(query, value)
        mydb.commit()
del data
