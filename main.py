import math

liczba_figur = int(input())

liczba_pi = math.pi

suma_pol = 0

def suma (liczba_figur, suma_pol):
    for i in range(liczba_figur):
        dane_figury = input()
        dane_figury = list(dane_figury.split(' '))
        if len(dane_figury) == 1:
            suma_pol = suma_pol + liczba_pi*float(dane_figury[0])**2
        elif len(dane_figury) == 2:
            suma_pol = suma_pol + float(dane_figury[0])*float(dane_figury[1])
        elif len(dane_figury) == 3:
            polowa_obwodu = float(dane_figury[0])/2 + float(dane_figury[1])/2 + float(dane_figury[2])/2
            suma_pol = suma_pol + math.sqrt(polowa_obwodu*(polowa_obwodu - float(dane_figury[0]))*(polowa_obwodu - float(dane_figury[1]))*(polowa_obwodu - float(dane_figury[2])))
        else: 
            wynik = 'Błąd: można podać maksymalnie 3 liczby'
            break
        wynik = round(suma_pol, 2)
    return wynik
print(suma(liczba_figur, suma_pol))