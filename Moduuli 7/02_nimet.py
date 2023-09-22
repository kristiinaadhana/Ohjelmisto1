nimet = set()

while True:
    syöte = str(input("Syötä nimiä: "))
    if syöte == "":
        break
    if syöte in nimet:
        print("Aiemmin syötetty nimi")
    else:
        nimet.add(syöte)

print("\nSyötetyt nimet:")
for syöte in nimet:
    print(syöte)






