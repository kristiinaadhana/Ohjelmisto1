kanta= float(input("Syötä suorakulmion kanta: "))
korkeus = float(input("Syötä suorakulmion korkeus: "))
piiri = float(kanta+kanta+korkeus+korkeus)
pinta = float(kanta*korkeus)

print("Suorakulmion piiri on  " + str(piiri) + "  ja pinta-ala  " + str(pinta))