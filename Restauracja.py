# coding: utf-8
 
class Kelner:
    def __init__(self):
        self.jedzenie = ["przystawka", "zupa", "danie główne"]
        self.ostatni_klient = None
 
    def serwowanie_jedzenia(self):
        zamowienie = input ("Proszę wybrać jedno z dań.\n")
        if zamowienie in self.jedzenie:
            print("Dziękuję. Proszę czekać. \n")
            print(f"Kelner : Kucharzu, następnym zamówieniem jest {zamowienie}, jak długo potrwa jego przyrządzenie?")
            return zamowienie
        else:
            print("Kelner : Żartowniś... Jedzenie, które wybrałeś nie jest dostępne. Zacznij od początku.")
           
    def przedstaw_menu(self):
        print(f'{self.ostatni_klient} znajdujesz się w restauracji. Podchodzi do Ciebie kelner. \n')
        print(f"Kelner : Witaj {self.ostatni_klient}, przedstawiam Tobie nasze menu.")
        print(self.jedzenie)
   
 
class Klient():
    def zam_jedzenia(self):
        imie = input ("Jak masz na imię? \n")
        return imie
 
class Kucharz():
    def __init__(self):
        self.czas_zamowienia = {'przystawka': "Kucharz: Jedzenie, które wybrałeś będzie gotowe w 10 minut. \n\n",
                      'zupa': "Kucharz: Jedzenie, które wybrałeś będzie gotowe w 15 minut. \n\n",
                      "danie główne": "Kucharz: Jedzenie, które wybrałeś będzie gotowe w 20 minut. \n\n"}
        self.zamowienie = None
   
    def przygotowanie_jedzenia(self):
        print(self.czas_zamowienia.get(self.zamowienie, 'Brak takiej potrawy'))
       
 
if __name__ == "__main__":
    kelner = Kelner()
    klient = Klient()
    Kucharz = Kucharz()
    kelner.ostatni_klient = klient.zam_jedzenia()
    kelner.przedstaw_menu()
    Kucharz.zamowienie = kelner.serwowanie_jedzenia()
    Kucharz.przygotowanie_jedzenia()