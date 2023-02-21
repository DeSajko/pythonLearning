# zabawa z __name__ == "__main__":
# importując plik .py w sprawiamy ze plik odrazu się uruchamia wykonując skrypt. Czasem tego nie chcemy ponieważ wcześniej mamy linijki kodu które nie mogą zostać pominięte i w takim przypadku z pomocą przychodzi nam:
#  __name__ == "__main__". Ta funkcja pozoli nam na importowanie funkcji z innego pliku za pomocą komendy nazwapliku.nazwaFunkcji() w tym przypadku: laczenie.imie(). Funkcja imie została napisana w pliku laczenie#

import laczenie

print("Czesc uzytkowniku")
username = laczenie.imie()

print("Siema", username)
