import mysql.connector

def HaeKentanTiedot(icao):
    sql= "select name, municipality from airport where ident = ' "+icao + "'";
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount>0:
        for rivi in tulos:
            print(rivi)


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='airport',
    user='Kristiina',
    password='12345',
    autocommit=True
)

icao = input('Anna haluamasi kentän ICAO-koodi: ')
HaeKentanTiedot(icao)
