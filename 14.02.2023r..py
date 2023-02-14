#----------------------------------------------------------------------------------------------------------------
# Pierwszy Projekt Pythonowy 14.02.2023r
#  
#   Skrypt/program Pythonowy pozwalający na dodawanie użytkowników oraz numerów telefonów za pomocą menu,
# po którym użytkownik porusza się przez funkcje inputowe wybierając możliwe opcje. 
# Użytkownicy są dodawani do listy co w przyszłości MUSI być poprawione i zastosowane w inny sposób,
# np za pomocą Folderów(Key:Value). 
# 
# Należy usprawnić o: 
#  - Użytkownicy dodawani w formie Key:Value;
#  - Zapisywanie użytkowników w notatniku/folderze;
#  - Dodanie numeracji użytkowników podczas edytowania ich;  
#  - MNIEJSZA ILOŚĆ ZMIENNYCH!!!
# --------------------------------------------------------------------------------------------------------------

dataBase = []
e = "\n--------------------------------\n"
s = "\n--------------------------------"

while True:
    print(s,"MENU:","1: Add new user","2: Edit User", "3: Show Users", "4: Quit", sep='\n',end = e)
    menu = input("Chose option by number: ")

# Menu dodania użytkownika     
    if menu == "1":
        menu1Resume = True
        while menu1Resume:
            print(e,"Add new user",e)
            userAddString = input("New User: ")
            dataBase.append(userAddString)
            print(e,"User:", userAddString,"added succesfuly",e,"\nDo you want add another user ?")
            while True:
                decision = input("Y/N: ")
                if decision.upper() == "N":
                    menu1Resume = False
                    break
                elif decision.upper() == "Y":
                    break
                else:
                    print("---Enter propertly!!!---")

# Wejście do menu edycyjnego
    elif menu == "2":
        print(e,"Edit",e)
        menu2Resume = True
        while menu2Resume:
            print(e,"1: Edit username", "2: Edit phone number", "3: Delete user", "4: Back", sep='\n', end = e)
            menu2Decision = input("Select option: ")
            
# Menu2 numer 1 pozwalające na edycję nazwy użytkownika
            while menu2Decision == "1":
                print(*dataBase, sep='\n')
                selectUser = input("User number: ")
                while int(selectUser) >= len(dataBase):
                    print("---There is not a user with that number !!!---")
                    break
                else:
                    print("You chose user", dataBase[int(selectUser)])
                    print(e,"Edit name for: ",dataBase[int(selectUser)],e)
                    editUser = input("New username: ")
                    dataBase[int(selectUser)] = editUser
                    exit = print(s,*dataBase,e,sep='\n')
                    print(e,"Do you want edit another user ?",e)
                    while True:
                        decision = input("Y/N: ")
                        if decision.upper() == "N":
                            menu2Decision = False
                            break
                        elif decision.upper() == "Y":
                            break
                        else:
                            print("---Enter propertly!!!---")
                            
# Menu2 numer 2 pozwalające na edycję numeru telefonu (w sumie można zmienić na przypisanie numeru telefonu lub usunięcie/edycję)
            while menu2Decision == "2":
                print(*dataBase, sep="\n")
                selectUser = input("User number:")
                while int(selectUser) >= len(dataBase):
                    print("---There is not a user with that number!!!---")
                    break
                else:
                    print("You chose user", dataBase[int(selectUser)])
                    user = dataBase[int(selectUser)]
                    numberForUser = input("Phone number: ")
                    userNumber = user+ " " +numberForUser
                    dataBase[int(selectUser)] = userNumber
                    print(numberForUser,"Has been added to", user)
                    print("Do you wan edit another phone number ?")
                    while True:
                        decision = input("Y/N: ")
                        if decision.upper() == "N":
                            menu2Decision = False
                            break
                        elif decision.upper() == "Y":
                            break
                        else:
                            print("---Enter propertly!!!---")
                    
                
                
# Menu2 numer 3 pozwalające na usunięnie użytkownika przez wybór liczby użytkownika                
            while menu2Decision == "3":
                print(*dataBase, sep='\n')
                selectUser = input("Select user by number to delete: ")
                deleteUser = int(selectUser)
                while deleteUser >= len(dataBase):
                    print("---There are not a user with this number!!!---", str(deleteUser))
                    break
                else:
                    print(e,"Do you want delete", dataBase[int(selectUser)],e)
                    decision = input("Y/N: ")
                    if decision.upper() == "N":
                        menu2Decision == False
                        break
                    elif decision.upper() == "Y":
                        print(e,"!!! User", dataBase[int(selectUser)],"deleted !!!",e)
                        dataBase.pop(deleteUser)
                        menu2Decision == False
                        break
                    else:
                        print("---Enter propertly!!!---")

#Menu2 4 pozwalające na wyjście z edycji
            if menu2Decision == "4":
                print(e,"Quit",e)
                break

# Menu wyświetlające użytkowników
    elif menu == "3":
        print(e,"Show Users",e)
        print(s,*dataBase, sep = "\n",end = e)

# Wyjście z programu
    elif menu == "4":
        print(e,"Quit",e)
        break
# Gdy użytkownik wybierze zły numer     
    else:
        print("---Chose right number---")     
