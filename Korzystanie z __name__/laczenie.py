def imie(username= ""):
    while True:
        name1 = input("Podaj swoje imię :")
        if name1.isdigit():
            print("To nie jest imię")
        else:
            username = name1
            return username           

if __name__ == '__main__':
    imie()
