f = open("kimi.csv", "r", encoding="utf-8")
f.readline


class Kimi:
    def __init__(self,Dat,NagyD,Hely,BefKor,Pont,Kon,Cel,KorH,Hiba):
        self.Dat = Dat
        self.NagyD = NagyD
        self.Hely = Hely
        self.BefKor = BefKor
        self.Pont = Pont
        self.Kon = Kon
        self.Cel = Cel
        self.KorH = KorH
        self.Hiba = Hiba
        
    def __str__(self):
        return f"{self.Dat} {self.NagyD} {self.Hely} {self.BefKor} {self.Pont} {self.Kon} {self.Cel} {self.KorH} {self.Hiba}"


db = -1 
lista = []

for sor in f:
    db += 1

print("3.feladat: ", db)

for sor in f:
    sor = sor.strip().split(";")
    lista.append(Kimi(sor[0],sor[1],sor[2],sor[3],sor[4],sor[5],sor[6],sor[7],sor[8]))

print("4.feladat: Magyar Nagydíj helyezései")
for elem in lista:
    if elem.NagyD == "Magyar Nagydíj":
        if elem.Cel == "I":
            print(f"{elem.Dat} {elem.Hely} hely")
    