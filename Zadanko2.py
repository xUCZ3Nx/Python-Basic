class Zabawa_z_list:
    def __init__(self):
        self.y = [1, 2, 2, 2, 3, 2]
    
    #Zadanie 1
    def Usun_dana_liczbe(self, a):
        for _ in range(len(self.y)):
            if a in self.y:
                self.y.remove(a)
        print(self.y)
        # for x in range(lista_pl.count(2)):
        #     lista_pl.remove(2)
    
    #Zadanie 2
    def Usun_dana_liczbe_while(self, a):
        while a in self.y:
            self.y.remove(a)
        print(self.y)

#Zadanie 3
    def Wypisz_co_2_element(self):
        for i in range(1,len(self.y),2):
            print(self.y[i])

#Zadanie 4
    def Wypisz_co_2_element_bez_range(self):
        x = []
        v = 1
        while v < len(self.y):
            x.append(v)
            v = v + 2
        #print(x) #sprawdzenie jaki mamy zakres
        for i in x:
            print(self.y[i])
        # for x in nasza_lista[1::2]:
        #     print(x)

#Zadanie 5
    def Wypisz_co_2_element_od_konca(self):
        x = []
        v = len(self.y) - 1
        while v > -1:
            x.append(self.y[v])
            v = v - 1
        #print(x) sprawdzenie czy lista jest wypisywana od końca
        for i in range(1,len(x),2):
            print(x[i])
        # for x in range(len(lista_testowa)-1,0,-2):
    #       print(lista_testowa[x])

#Zadanie 6
    def Wypisz_co_2_element_od_konca_bez_range(self):
        x = []
        v = len(self.y) - 1
        while v > -1:
            x.append(self.y[v])
            v = v - 1
        #print(x) sprawdzenie czy lista jest wypisywana od końca
        c = []
        z = 1
        while z < len(x):
            c.append(z)
            z = z + 2
        #print(x) #sprawdzenie jaki mamy zakres
        for i in c:
            print(x[i])
        # for x in lista_testowa[-1::-2]:
        #     print(x)

#Zadanie 7
    def Lista_zawierajaca_krotki(self):
        
        Nowa_lista = []

        for i in range(len(self.y)):
            krotka2 = (i, self.y[i])
            Nowa_lista.append(krotka2)
        print(Nowa_lista)

    def Lista_skladana_zawierajaca_krotki(self):
        Nowa_lista = [(i, self.y[i]) for i in range(len(self.y))]
        print(Nowa_lista)

#Zadanie 8
    def Sortowanie_listy_wg_2_elementu_krotek(self):
        Nowa_lista = [(i, self.y[i]) for i in range(len(self.y))]

        Posortowana_Nowa_lista = sorted(
            Nowa_lista, key=lambda Tomasz_kutasie_daj_cos_trudniejszego: Tomasz_kutasie_daj_cos_trudniejszego[1])
        print(Posortowana_Nowa_lista)

#Zadanie 9
    def Lista_skladana_zawierajaca_krotki_wartosci_parzystych(self):
        Nowa_lista = [(i, self.y[i]) for i in range(len(self.y)) if self.y[i] % 2 == 0]
        print(Nowa_lista)

#zadanie 10
    def Lista_skladana_zawierajaca_posegregowane_wewnatrz_roznaco(self):
        Nowa_lista = [(i, self.y[i]) if i <= self.y[i] else (self.y[i], i) for i in range(len(self.y))]
        print(Nowa_lista)
Zabawa_z_list().Lista_skladana_zawierajaca_posegregowane_wewnatrz_roznaco()
