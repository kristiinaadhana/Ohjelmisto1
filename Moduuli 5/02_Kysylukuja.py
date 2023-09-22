luvut = []

while True:

    luku = (input("Anna seuraava luku tai lopeta painamalla enter: "))
    if luku == "":
        break
    luvut.append(int(luku))
luvut.sort(reverse=True)
print(luvut[:5])
