import random

lukumäärä = int(input("Syötä arpakuutioiden lukumäärä: "))
summa=0
for i in range(lukumäärä):
    silmäluku = random.randint(1,6)
    summa+= silmäluku
    print(f"Arpakuution heitto {i+1}: {silmäluku}")
print(f"silmälukujen summa: {summa}")
