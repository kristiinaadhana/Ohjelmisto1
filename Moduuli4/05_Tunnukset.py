Käyttäjänimi = str(input("Syötä käyttäjänimi: "))
Salasana = str(input("Syötä salasana: "))
tehdyt=0

while Käyttäjänimi!="python" or Salasana!="rules":
    print('Pääsy evätty! Yritä uudelleen.')
    Käyttäjänimi= input("Syötä käyttäjänimi: ")
    Salasana = input("Syötä salsana: ")
    tehdyt = tehdyt+1
    if tehdyt == 4:
        break
else:
    print("Tervetuloa!:)")
