while True:
    Tuuma = float(input("Syötä tuumamäärä: "))
    Sentti = Tuuma * 2.54

    if Tuuma > 0:
        print(f"Antamasi tuuma on sentteinä {Sentti}")
    elif Tuuma < 0:
        break