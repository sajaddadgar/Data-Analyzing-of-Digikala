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
cursor.execute("create database if not exists mytest;")
cursor.execute("use mytest;")

# Create a table for mobile, laptop, tablet, gaming console, headphone, speaker
cursor.execute("create table if not exists mobile " 
               "(id int, "
               "title_fa varchar(255), "
               "title_en varchar(255), "
               "url_code varchar(255), "
               "category_fa varchar(255), "
               "keywords varchar(255), "
               "brand_fa varchar(255), "
               "brand_en varchar(255), "
               "primary key (id));")

cursor.execute("create table if not exists laptop "
               "(id int primary key , "
               "title_fa varchar(255), "
               "title_en varchar(255), "
               "url_code varchar(255), "
               "category_fa varchar(255), "
               "keywords varchar(255), "
               "brand_fa varchar(255), "
               "brand_en varchar(255));")
cursor.execute("create table if not exists tablet "
               "(id int primary key , "
               "title_fa varchar(255), "
               "title_en varchar(255), "
               "url_code varchar(255), "
               "category_fa varchar(255), "
               "keywords varchar(255), "
               "brand_fa varchar(255), "
               "brand_en varchar(255));")
cursor.execute("create table if not exists gamingconsole "
               "(id int primary key , "
               "title_fa varchar(255), "
               "title_en varchar(255), "
               "url_code varchar(255), "
               "category_fa varchar(255), "
               "keywords varchar(255), "
               "brand_fa varchar(255), "
               "brand_en varchar(255));")
cursor.execute("create table if not exists headphone "
               "(id int primary key , "
               "title_fa varchar(255), "
               "title_en varchar(255), "
               "url_code varchar(255), "
               "category_fa varchar(255), "
               "keywords varchar(255), "
               "brand_fa varchar(255), "
               "brand_en varchar(255));")
cursor.execute("create table if not exists speaker "
               "(id int primary key , "
               "title_fa varchar(255), "
               "title_en varchar(255), "
               "url_code varchar(255), "
               "category_fa varchar(255), "
               "keywords varchar(255), "
               "brand_fa varchar(255), "
               "brand_en varchar(255));")

# Create a table for attribute of mobile, laptop, tablet, gaming console, headphone, speaker
cursor.execute("create table if not exists laptop_attribute "
               "(id int auto_increment, "
               "product_id int, "
               "x varchar(255) default null , "
               "y varchar(255) default null,"
               "screens varchar(255) default null,"
               "usb varchar(255) default null,"
               "ram varchar(255) default null,"
               "primary key (id),"
               "foreign key (product_id) references laptop(id));")
cursor.execute("create table if not exists headphone_attribute "
               "(id int auto_increment, "
               "product_id int, "
               "x varchar(255), "
               "y varchar(255),"
               "weight varchar(255),"
               "lenght varchar(255),"
               "primary key (id),"
               "foreign key (product_id) references headphone(id));")

# Create a table for description of mobile, laptop, tablet, gaming console, headphone, speaker
cursor.execute("create table if not exists title_alt_for_mobile "
               "(id int auto_increment, "
               "product_id int, "
               "description varchar(255),"
               "primary key (id),"
               "foreign key (product_id) references mobile(id));")
cursor.execute("create table if not exists title_alt_for_laptop "
               "(id int auto_increment, "
               "product_id int, "
               "description varchar(255),"
               "primary key (id),"
               "foreign key (product_id) references laptop(id));")
cursor.execute("create table if not exists title_alt_for_tablet "
               "(id int auto_increment, "
               "product_id int, "
               "description varchar(255),"
               "primary key (id),"
               "foreign key (product_id) references tablet(id));")
cursor.execute("create table if not exists title_alt_for_gamingconsole "
               "(id int auto_increment, "
               "product_id int, "
               "description varchar(255),"
               "primary key (id),"
               "foreign key (product_id) references gamingconsole(id));")
cursor.execute("create table if not exists title_alt_for_headphone "
               "(id int auto_increment, "
               "product_id int, "
               "description varchar(255),"
               "primary key (id),"
               "foreign key (product_id) references headphone(id));")
cursor.execute("create table if not exists title_alt_for_speaker "
               "(id int auto_increment, "
               "product_id int, "
               "description varchar(255),"
               "primary key (id),"
               "foreign key (product_id) references speaker(id));")

# Read Product related file
info = pd.read_excel("data/5-awte8wbd.xlsx")

# List of attributes
head = list(info)

# Insert each columns and values in arrays
col = []
for i in range(head.__len__()):
    col.append(pd.DataFrame(info, columns=[head[i]]))
info_value = []
for i in range(head.__len__()):
    info_value.append(col[i].get_values())

# Product's title
mobile_title=r'گوشی موبایل'
laptop_title='لپ تاپ و الترابوک'
tablet_title='تبلت'
gamingconsole_title='کنسول خانگی'
headphone_title='هدفون'
speaker_title='اسپیکر'

# Get index and values for filtering products
target_index=head.index('category_title_fa')
title_alt_index=head.index('title_alt')
target_title=col[target_index].get_values()
title_alt_val=col[title_alt_index].get_values()

# Insert mobile's data into tables
cursor.execute('select * from mobile')
data=cursor.fetchall()
# This part check mobile's table is empty or not, if table is'nt empty, no action is needed
if not data:
# Filter mobiles
    for i in range(col[target_index].__len__()):
        if re.search(mobile_title, target_title[i][0]):

            query= """insert into mobile (
                        id, title_fa, title_en, url_code, category_fa, keywords, brand_fa, brand_en)
                        values (%s, %s, %s, %s, %s, %s, %s, %s)"""
            # insert values of cells without brackets and parantheses and quotation marks
            value=(int(info_value[0][i]),
                    str(info_value[1][i])[2:len(str(info_value[1][i]))-2],
                    str(info_value[2][i])[1:len(str(info_value[2][i]))-1],
                    str(info_value[3][i])[2:len(str(info_value[3][i]))-2],
                    str(info_value[5][i])[2:len(str(info_value[5][i]))-2],
                    str(info_value[6][i])[2:len(str(info_value[6][i]))-2],
                    str(info_value[7][i])[2:len(str(info_value[7][i]))-2],
                    str(info_value[8][i])[2:len(str(info_value[8][i]))-2])
            # Insert operation
            cursor.execute(query, value)
            mydb.commit()



            # Insert title_alt's data into another table
            x = info_value[4][i]
            # Split strings in title_alt and insert into table
            title_alt_array = re.split('،|,|-', str(x[0]))
            for row in title_alt_array:
                query2="""insert into title_alt_for_mobile (
                            product_id, description)
                            values (%s, %s)"""
                value2=(int(info_value[0][i]), row)
                cursor.execute(query2, value2)
                mydb.commit()
            del x, title_alt_array
del data

# Insert laptop's data into tables
cursor.execute('select * from laptop')
data=cursor.fetchall()
# This part check laptop's table is empty or not, if table is'nt empty, no action is needed
if not data:
# Filter laptops
    for i in range(col[target_index].__len__()):
        if re.search(laptop_title, target_title[i][0]):
            query= """insert into laptop(
                        id, title_fa, title_en, url_code, category_fa, keywords, brand_fa, brand_en)
                        values (%s, %s, %s, %s, %s, %s, %s, %s)"""
            # insert values of cells without brackets and parantheses and quotation marks
            value=(int(info_value[0][i]),
                    str(info_value[1][i])[2:len(str(info_value[1][i]))-2],
                    str(info_value[2][i])[1:len(str(info_value[2][i]))-1],
                    str(info_value[3][i])[2:len(str(info_value[3][i]))-2],
                    str(info_value[5][i])[2:len(str(info_value[5][i]))-2],
                    str(info_value[6][i])[2:len(str(info_value[6][i]))-2],
                    str(info_value[7][i])[2:len(str(info_value[7][i]))-2],
                    str(info_value[8][i])[2:len(str(info_value[8][i]))-2])
            # Insert operation
            cursor.execute(query, value)
            mydb.commit()

            # Insert attribute's data (product_attribute) into tables
            listOfJson=str(info_value[9][i])[3:len(str(info_value[9][i]))-3]
            myjson = re.split("},", listOfJson)
            if myjson[myjson.__len__()-1]!="":
                jj = myjson[myjson.__len__()-1]
                for item in range(myjson.__len__()-1):
                    kk = myjson[item]+"}"
                    lo = json.loads(kk)
                    sqlQuery = """insert into laptop_attribute (
                                   product_id)
                                   values (%s)"""
                    sqlValue = (int(info_value[0][i]), )
                    cursor.execute(sqlQuery, sqlValue)

                    if lo["Key"]=='مشخصات حافظه داخلی':
                        updateQuery1 = """update laptop_attribute set x=%s where product_id=%s"""
                        if "Value" not in lo:
                            valueUpdate1 = ("", int(info_value[0][i]))
                        else:
                            valueUpdate1 = (lo["Value"], int(info_value[0][i]))

                        cursor.execute(updateQuery1, valueUpdate1)
                        mydb.commit()

                    if lo["Key"]=='توضیحات پورت شبکه Ethernet':
                        updateQuery1 = """update laptop_attribute set y=%s where product_id=%s"""
                        valueUpdate1 = (lo["Value"], int(info_value[0][i]))
                        cursor.execute(updateQuery1, valueUpdate1)
                        mydb.commit()

                    if lo["Key"]=='صفحه نمایش لمسی':
                        updateQuery1 = """update laptop_attribute set screens=%s where product_id=%s"""
                        valueUpdate1 = (lo["Value"], int(info_value[0][i]))
                        cursor.execute(updateQuery1, valueUpdate1)
                        mydb.commit()

                    if lo["Key"]=='پورت USB Type-C':
                        updateQuery1 = """update laptop_attribute set usb=%s where product_id=%s"""
                        valueUpdate1 = (lo["Value"], int(info_value[0][i]))
                        cursor.execute(updateQuery1, valueUpdate1)
                        mydb.commit()

                    if lo["Key"]=='نوع حافظه RAM':
                        updateQuery1 = """update laptop_attribute set ram=%s where product_id=%s"""
                        valueUpdate1 = (lo["Value"], int(info_value[0][i]))
                        cursor.execute(updateQuery1, valueUpdate1)
                        mydb.commit()

            myquery="""delete from laptop_attribute where x is null;"""
            cursor.execute(myquery)
            mydb.commit()



            # Insert title_alt's data into another table
            x = info_value[4][i]
            # Split strings in title_alt and insert into table
            title_alt_array = re.split('،|,|-', str(x[0]))
            for row in title_alt_array:
                query2="""insert into title_alt_for_laptop (
                            product_id, description)
                            values (%s, %s)"""
                value2=(int(info_value[0][i]), row)
                cursor.execute(query2, value2)
                mydb.commit()
            del x, title_alt_array
del data

# Insert tablet's data into tables
cursor.execute('select * from tablet')
data=cursor.fetchall()
# This part check tablet's table is empty or not, if table is'nt empty, no action is needed
if not data:
# Filter tablets
    for i in range(col[target_index].__len__()):
        if re.search(tablet_title, target_title[i][0]):
            query= """insert into tablet(
                        id, title_fa, title_en, url_code, category_fa, keywords, brand_fa, brand_en)
                        values (%s, %s, %s, %s, %s, %s, %s, %s)"""
            # insert values of cells without brackets and parantheses and quotation marks
            value=(int(info_value[0][i]),
                    str(info_value[1][i])[2:len(str(info_value[1][i]))-2],
                    str(info_value[2][i])[1:len(str(info_value[2][i]))-1],
                    str(info_value[3][i])[2:len(str(info_value[3][i]))-2],
                    str(info_value[5][i])[2:len(str(info_value[5][i]))-2],
                    str(info_value[6][i])[2:len(str(info_value[6][i]))-2],
                    str(info_value[7][i])[2:len(str(info_value[7][i]))-2],
                    str(info_value[8][i])[2:len(str(info_value[8][i]))-2])
            # Insert operation
            cursor.execute(query, value)
            mydb.commit()

            # Insert title_alt's data into another table
            x = info_value[4][i]
            # Split strings in title_alt and insert into table
            title_alt_array = re.split('،|,|-', str(x[0]))
            for row in title_alt_array:
                query2="""insert into title_alt_for_tablet (
                            product_id, description)
                            values (%s, %s)"""
                value2=(int(info_value[0][i]), row)
                cursor.execute(query2, value2)
                mydb.commit()
            del x, title_alt_array
del data

# Insert gaming console's data into tables
cursor.execute('select * from gamingconsole')
data=cursor.fetchall()
# This part check gaming console's table is empty or not, if table is'nt empty, no action is needed
if not data:
# Filter gaming consoles
    for i in range(col[target_index].__len__()):
        if re.search(gamingconsole_title, target_title[i][0]):
            query= """insert into gamingconsole(
                        id, title_fa, title_en, url_code, category_fa, keywords, brand_fa, brand_en)
                        values (%s, %s, %s, %s, %s, %s, %s, %s)"""
            # insert values of cells without brackets and parantheses and quotation marks
            value=(int(info_value[0][i]),
                    str(info_value[1][i])[2:len(str(info_value[1][i]))-2],
                    str(info_value[2][i])[1:len(str(info_value[2][i]))-1],
                    str(info_value[3][i])[2:len(str(info_value[3][i]))-2],
                    str(info_value[5][i])[2:len(str(info_value[5][i]))-2],
                    str(info_value[6][i])[2:len(str(info_value[6][i]))-2],
                    str(info_value[7][i])[2:len(str(info_value[7][i]))-2],
                    str(info_value[8][i])[2:len(str(info_value[8][i]))-2])
            # Insert operation
            cursor.execute(query, value)
            mydb.commit()

            # Insert title_alt's data into another table
            x = info_value[4][i]
            # Split strings in title_alt and insert into table
            title_alt_array = re.split('،|,|-', str(x[0]))
            for row in title_alt_array:
                query2="""insert into title_alt_for_gamingconsole (
                            product_id, description)
                            values (%s, %s)"""
                value2=(int(info_value[0][i]), row)
                cursor.execute(query2, value2)
                mydb.commit()
            del x, title_alt_array
del data

# Insert headphone's data into tables
cursor.execute('select * from headphone')
data=cursor.fetchall()
# This part check headphone's table is empty or not, if table is'nt empty, no action is needed
if not data:
# Filter headphones
    for i in range(col[target_index].__len__()):
        if re.search(headphone_title, target_title[i][0]):
            query= """insert into headphone(
                        id, title_fa, title_en, url_code, category_fa, keywords, brand_fa, brand_en)
                        values (%s, %s, %s, %s, %s, %s, %s, %s)"""
            # insert values of cells without brackets and parantheses and quotation marks
            value=(int(info_value[0][i]),
                    str(info_value[1][i])[2:len(str(info_value[1][i]))-2],
                    str(info_value[2][i])[1:len(str(info_value[2][i]))-1],
                    str(info_value[3][i])[2:len(str(info_value[3][i]))-2],
                    str(info_value[5][i])[2:len(str(info_value[5][i]))-2],
                    str(info_value[6][i])[2:len(str(info_value[6][i]))-2],
                    str(info_value[7][i])[2:len(str(info_value[7][i]))-2],
                    str(info_value[8][i])[2:len(str(info_value[8][i]))-2])
            # Insert operation
            cursor.execute(query, value)
            mydb.commit()

            # Insert attribute's data (product_attribute) into tables
            listOfJson = str(info_value[9][i])[3:len(str(info_value[9][i])) - 3]
            myjson = re.split("},", listOfJson)
            if myjson[myjson.__len__() - 1] != "":
                jj = myjson[myjson.__len__() - 1]
                for item in range(myjson.__len__() - 1):
                    kk = myjson[item] + "}"
                    lo = json.loads(kk)
                    sqlQuery = """insert into headphone_attribute (
                                                       product_id)
                                                       values (%s)"""
                    sqlValue = (int(info_value[0][i]),)
                    cursor.execute(sqlQuery, sqlValue)

                    if lo["Key"] == 'ابعاد':
                        updateQuery1 = """update headphone_attribute set x=%s where product_id=%s"""
                        valueUpdate1 = (lo["Value"], int(info_value[0][i]))
                        cursor.execute(updateQuery1, valueUpdate1)
                        mydb.commit()

                    if lo["Key"] == 'رابط':
                        updateQuery1 = """update headphone_attribute set y=%s where product_id=%s"""
                        valueUpdate1 = (lo["Value"], int(info_value[0][i]))
                        cursor.execute(updateQuery1, valueUpdate1)
                        mydb.commit()

                    if lo["Key"] == 'وزن':
                        updateQuery1 = """update headphone_attribute set weight=%s where product_id=%s"""
                        valueUpdate1 = (lo["Value"], int(info_value[0][i]))
                        cursor.execute(updateQuery1, valueUpdate1)
                        mydb.commit()

                    if lo["Key"] == 'طول کابل':
                        updateQuery1 = """update headphone_attribute set lenght=%s where product_id=%s"""
                        valueUpdate1 = (lo["Value"], int(info_value[0][i]))
                        cursor.execute(updateQuery1, valueUpdate1)
                        mydb.commit()
                myquery = """delete from headphone_attribute where x is null and id!=1;"""
                cursor.execute(myquery)
                mydb.commit()


            # Insert title_alt's data into another table
            x = info_value[4][i]
            # Split strings in title_alt and insert into table
            title_alt_array = re.split('،|,|-', str(x[0]))
            for row in title_alt_array:
                query2="""insert into title_alt_for_headphone (
                            product_id, description)
                            values (%s, %s)"""
                value2=(int(info_value[0][i]), row)
                cursor.execute(query2, value2)
                mydb.commit()
            del x, title_alt_array
del data

# Insert speaker's data into tables
cursor.execute('select * from speaker')
data=cursor.fetchall()
# This part check speaker's table is empty or not, if table is'nt empty, no action is needed
if not data:
# Filter speakers
    for i in range(col[target_index].__len__()):
        if re.search(speaker_title, target_title[i][0]):
            query= """insert into speaker(
                        id, title_fa, title_en, url_code, category_fa, keywords, brand_fa, brand_en)
                        values (%s, %s, %s, %s, %s, %s, %s, %s)"""
            # insert values of cells without brackets and parantheses and quotation marks
            value=(int(info_value[0][i]),
                    str(info_value[1][i])[2:len(str(info_value[1][i]))-2],
                    str(info_value[2][i])[1:len(str(info_value[2][i]))-1],
                    str(info_value[3][i])[2:len(str(info_value[3][i]))-2],
                    str(info_value[5][i])[2:len(str(info_value[5][i]))-2],
                    str(info_value[6][i])[2:len(str(info_value[6][i]))-2],
                    str(info_value[7][i])[2:len(str(info_value[7][i]))-2],
                    str(info_value[8][i])[2:len(str(info_value[8][i]))-2])
            # Insert operation
            cursor.execute(query, value)
            mydb.commit()

            # Insert title_alt's data into another table
            x = info_value[4][i]
            # Split strings in title_alt and insert into table
            title_alt_array = re.split('،|,|-', str(x[0]))
            for row in title_alt_array:
                query2="""insert into title_alt_for_speaker (
                            product_id, description)
                            values (%s, %s)"""
                value2=(int(info_value[0][i]), row)
                cursor.execute(query2, value2)
                mydb.commit()
            del x, title_alt_array
del data
