from operator import truediv


GoOrOk = True


def kozSoruSor():
    str(input("Arttırmak istiyor musun? (y/n): "))

def arttirMiktar():
    int(input("Ne kadar arttırmak istiyorsun? (tam sayı belirt): "))


A = str(kozSoruSor())
if A == "y":
    arttirMiktar()

