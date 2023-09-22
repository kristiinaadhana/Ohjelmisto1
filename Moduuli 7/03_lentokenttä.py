Lentokenttä = {}

while True:
    Lentoasema = str(input("Syötä uusi lentoasema valitsemalla 1, hae lentoasemaa valitsemalla 2 tai lopeta painamalla enter: "))
    if Lentoasema == "1":
        Lentonimi = input("Syötä lentoaseman nimi: ")
        ICAO = input("Syötä lentoaseman ICAO-koodi: ")
    Lentokenttä[ICAO]= Lentonimi
    if Lentoasema == "2":
        input("Syötä ICAO-koodi: ")
        if Lentoasema in ICAO:
             print(f"Lentoasema on: {Lentokenttä}")
    elif Lentoasema == "":
        break
    else:
        print("Syötä vastaus uudelleen")
        

       
# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden
# lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma
# kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä
# vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten
# monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi
# Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)