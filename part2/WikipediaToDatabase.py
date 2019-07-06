from bs4 import BeautifulSoup
import requests
import pandas as pd
import mysql.connector

URL = 'https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D8%B4%D9%87%D8%B1%D9%87%D8%A7%DB%8C_%D8%A7%DB%8C%D8%B1%D8%A7%D9%86_%D8%A8%D8%B1_%D9%BE%D8%A7%DB%8C%D9%87_%D8%AC%D9%85%D8%B9%DB%8C%D8%AA'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

mydb = mysql.connector.connect(host="localhost", user="root", password="java123")
cursor = mydb.cursor()
cursor.execute("use mytest2;")

cursor.execute("create table city_population  " 
               "(id int primary key auto_increment,"
               "name varchar(255),"
               "population int);")



table = soup.find('table', {'class':'wikitable sortable'}).tbody

rows = table.find_all('tr')
columns = [v.text.replace("\n", "") for v in rows[0].find_all('th')]

df = pd.DataFrame(columns=columns)
query = "insert into city_population (name, population) values (%s, %s)"

for i in range(1, len(rows)):
    tds = rows[i].find_all('td')
    x = tds[4].text.replace('٬', '')
    values = [tds[0].text, int(x.replace('[پاورقی ۴]', ''))]

    print(int(x.replace('[پاورقی ۴]', '')))
    cursor.execute(query, values)
    mydb.commit()
