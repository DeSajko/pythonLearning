# Pierwsza styczność z funkcjami def. Postanowiłem napisać prosty skrypt który za pomocą defów wykonuje mnożenie oraz weryfikuje czy podana wartość jest liczbą.
# DO zapamiętania, gdy w Def'ie są dwie zmienne to powstaje z nich tuple !!!. Gdy chcemy z tupla wyciągnąć pojedynczą wartość to korzystamy z [] i wpisujemy pozycję która nas interesuje.
def mnozenie(x,y):
    print("Wynik mnożenia",x,"*",y,"to:", x*y)

def systemWeryfikacja(num1 = 0,num2 =0):
    num1 = 0
    while True:
        zmienna1 = input("Wprowadz pierwszą liczbę: ")
        zmiennaCheck1 = zmienna1.isdigit()
        if zmiennaCheck1 == True:
            print("Pierwsza liczba jest poprawna")
            liczba1 = int(zmienna1)
            print(type(liczba1),"\n", liczba1)
            num1 = liczba1
            break
        else:
            print("Zła wartość")
    num2 = 0
    while True:
        zmienna2 = input("Wprowadz drugą liczbę: ")
        zmiennacheck2 = zmienna2.isdigit()
        if zmiennacheck2 == True:
            print("Druga liczba jest poprawna")
            liczba2 = int(zmienna2)
            print(type(liczba2), "\n",liczba2)
            num2 = liczba2
            break
        else:
            print("Zła wartość")
    return num1, num2

wynik = systemWeryfikacja()
x = wynik[0]
y = wynik[1]

mnozenie(x,y)


