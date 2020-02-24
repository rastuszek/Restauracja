# coding: utf-8

import random

ruchy = ["kamień", "nożyce", "papier"]

def uderzenia (jeden, dwa):
    return ((jeden == "kamień" and dwa == "nożyce") or
            (jeden == "nożyce" and dwa == "papier") or
            (jeden == "papier" and dwa == "kamień"))
    
class Gracz:
    def ruch (self):
        return "kamień"
    
    def uczenie(self, mojruch, ichruch):
        pass
        
class LosowyGracz(Gracz):
        def ruch (self):
            return (random.choice(ruchy))

class LudzkiGracz(Gracz):
    def ruch(self):
        ruch = input ("Kamień, nożyce czy papier?")
        while ruch.lower().strip() not in ruchy:
            print("Przepraszam, ale nie rozumiem. Spróbuj jeszcze raz.")
            ruch = input ("Proszę wybrać kamień, nożyce lub papier.")
        return ruch
        

class Gra():   
    def __init__(self, p1, p2):
        self.g1 = LudzkiGracz()
        self.g2 = p2
        self.g1_zestawienie = 0
        self.g2_zestawienie = 0

    def tura(self):
        ruch1 = self.g1.ruch()
        ruch2 = self.g2.ruch()
        print(f"Gracz 1: {ruch1}  Gracz 2: {ruch2}")
        self.g1.uczenie(ruch1, ruch2)
        self.g2.uczenie(ruch2, ruch1)
        self.wynik(ruch1, ruch2)
    
    def wynik(self, ruch1, ruch2):
        if uderzenia(ruch1, ruch2):
            self.g1_zestawienie += 1
            print(f"Ty: {self.g1_zestawienie}  Przeciwnik: {self.g2_zestawienie}")
        elif uderzenia(ruch2, ruch1):
            self.g2_zestawienie += 1
            print(f"Ty: {self.g1_zestawienie}  Przeciwnik: {self.g2_zestawienie}")
        elif ruch1 == ruch2:
            print("Remis! Bez punktu dla Ciebie i przeciwnika.")
        
    def uruchom(self):
        print("Rozpoczęcie gry")
        for round in [1,2,3,4,5]:
            print(f"Runda {round}:")
            self.tura()
        if self.g1_zestawienie > self.g2_zestawienie:
                print("Wygrałeś!")
        elif self.g2_zestawienie > self.g1_zestawienie:
                print ("Przegrałeś!")
        elif self.g1_zestawienie == self.g2_zestawienie:
                print("Remis!")

if __name__ == '__main__':
    gra = Gra(LudzkiGracz(), LosowyGracz())
    gra.uruchom()