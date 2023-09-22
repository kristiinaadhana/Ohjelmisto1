Kokonaisluku=int(input("Syötä kokonaisluku: "))

on_alkuluku = True
for jakaja in range(2, Kokonaisluku):
    if Kokonaisluku % jakaja == 0:
        on_alkuluku=False
if on_alkuluku:
    print("Luku on alkuluku")
else: print('Luku ei ole alkuluku')

