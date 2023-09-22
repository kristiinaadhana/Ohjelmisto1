import random
def heitto():
    return random.randint(1,6)

while True:
    heitto = str(input("Heitä noppaa painamalla enter: "))
    silmäluku = heitto()
    print(f"heitto {silmäluku}")
    if silmäluku == 6:
        break

print("Sait kuutosen")
