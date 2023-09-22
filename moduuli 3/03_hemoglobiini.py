sukupuoli = (str(input("Anna sukupuoli: ")))
hemoglobiini = float(input("Anna hemoglobiini: "))

if 'nainen'and (hemoglobiini<175 and hemoglobiini>117):
    print("Hemoglobiiniarvo on normaali")
elif "nainen" and (hemoglobiini<117):
    print("Hemoglobiiniarvo on alhainen")
elif "nainen" and (hemoglobiini>175):
    print("Hemoglobiiniarvo on korkea")

elif "mies" and (134<=hemoglobiini<=195):
    print("Hemoglobiiniarvo on normaali")
elif "mies" and (hemoglobiini<134):
    print("Hemoglobiiniarvo on alhainen")
elif "mies" and (hemoglobiini>195):
    print("Hemoglobiiniarvo on korkea")
