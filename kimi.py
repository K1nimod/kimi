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
        return(f"{self.Dat} {self.NagyD} {self.Hely} {self.BefKor} {self.Pont} {self.Kon} {self.Cel} {self.KorH} {self.Hiba}")


f = open('kimi.csv', 'rt', encoding='UTF-8')
f.readline()

lista = []
db = 0
for sor in f:
    db += 1 
    sor = sor.strip().split(';')
    lista.append(Kimi(sor[0], sor[1], sor[2], sor[3], sor[4], sor[5], sor[6], sor[7], sor[8]))

print('3. feladat:', db)

print('4. feladat: Magyar Nagydíj helyezései')
for elem in lista:
    if elem.NagyD == 'Magyar Nagydíj':
        if elem.Cel == 'I':
            print(f'{elem.Dat}: {elem.Hely} helyezés')

print('5. feladat: Hibastatisztika')

hib = {}

for hiba in lista:
    if hiba.Hiba not in hib.keys():
        hib[hiba.Hiba] = 1
    else:
        hib[hiba.Hiba] += 1

for k, v in hib.items():
    if v > 1:
        print(f'{k}: {v}')