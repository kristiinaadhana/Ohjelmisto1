def litra():
    gallonamäärä = int(input("Syötä määrä gallonina: "))
    litramäärä = gallonamäärä*3.785
    print(f"Antamasi gallonat on litroina {litramäärä} litraa")
    return litramäärä

while True:
    litrat = litra()
    if litrat < 0:
        break











