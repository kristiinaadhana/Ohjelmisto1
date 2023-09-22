Kuha = float(input("Syötä kuhan pituus sentteinä: "))
Kasvu = Kuha - 37
if Kuha < 37:
    print("Kuha on liian pieni, laske se takaisin järveen!" + " Sen täytyy kasvaa vielä " + str(Kasvu) + "cm")
if Kuha > 36:
    print("Kuha on tarpeeksi iso!")