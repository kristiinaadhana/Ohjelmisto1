kaupungit = []
for i in range(5):
    kaupunki = input(f"Syötä kaupunki {i+1}: ")
    kaupungit.append(kaupunki)

print("Syöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)
