import random

satunnainen = random.randint(1,10)

while True:
    Luku = int(input("Arvaa luku: "))
    if satunnainen > Luku:
        print("Liian pieni arvaus!")
    elif satunnainen < Luku:
        print("Liian suuri arvaus")
    elif satunnainen == Luku:
        print("Oikein!")
        break

