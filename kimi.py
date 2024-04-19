f = open("kimi.csv" "r" encoding="utf-8")
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


