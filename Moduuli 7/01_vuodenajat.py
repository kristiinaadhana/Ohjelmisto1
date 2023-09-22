kuukausi = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
järjestysnumero = int(input("Syötä kuukauden numero: "))
kuukaudet = kuukausi[järjestysnumero-1]
print(f"{järjestysnumero} kuukausi on {kuukaudet}")
