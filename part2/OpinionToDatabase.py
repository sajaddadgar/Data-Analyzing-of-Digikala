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
cursor.execute("create table opinion" 
               "(id int primary key auto_increment,"
               "product_id int,"
               "product_title varchar(255),"
               "title_en varchar(255),"
               "user_id int,"
               "likes int,"
               "dislikes int,"
               "verification_status varchar(30),"
               "recommend varchar(255),"
               "title varchar(255),"
               "comment varchar(255),"
               "advantages varchar(30),"
               "disadvantages varchar(30));")

info = pd.read_excel("data/2-p9vcb5bb.xlsx")
head = list(info)

col = []
for i in range(head.__len__()):
    col.append(pd.DataFrame(info, columns=[head[i]]))
info_value = []
for i in range(head.__len__()):
    info_value.append(col[i].get_values())


cursor.execute('select * from opinion')
data=cursor.fetchall()
# This part check mobile's table is empty or not, if table is'nt empty, no action is needed
if not data:
# Filter mobiles
    for i in range(col[0].__len__()):

        query= """insert into opinion (
                    product_id, product_title, title_en, user_id, likes, dislikes,
                     verification_status, recommend, title, comment, advantages, disadvantages)
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        # insert values of cells without brackets and parantheses and quotation marks
        value=(int(info_value[0][i]),
                str(info_value[1][i])[2:len(str(info_value[1][i]))-2],
                str(info_value[2][i])[2:len(str(info_value[2][i]))-2],
                int(info_value[3][i]),
                int(info_value[4][i]),
                int(info_value[5][i]),
                str(info_value[6][i])[2:len(str(info_value[6][i]))-2],
                str(info_value[7][i])[2:len(str(info_value[7][i]))-2],
                str(info_value[8][i])[2:len(str(info_value[8][i]))-2],
                str(info_value[9][i])[2:len(str(info_value[9][i]))-2],
                str(info_value[10][i])[2:len(str(info_value[10][i]))-2],
                str(info_value[11][i])[2:len(str(info_value[11][i]))-2])
        # Insert operation
        try:
            cursor.execute(query, value)
        except mysql.connector.errors.DataError:
            print('')
        mydb.commit()
del data
