def gender():
#CPM = PPM x współczynnik aktywności fizycznej
#Wartość współczynnika aktywności fizycznej	Stopień aktywności fizycznej
#1,2	brak (osoba chora, leżąca w łóżku)
#1,4	mała (osoba wykonująca pracę siedzącą)
#1,6	umiarkowana (osoba wykonująca pracę na stojąco)
#1,75	duża (osoba prowadząca aktywny tryb życia, regularnie ćwicząca)
#2,0	bardzo duża (osoba prowadząca bardzo aktywny tryb życia, codziennie ćwicząca)
#2,4	osoba zawodowo uprawiająca sport

#dla kobiet: PPM = 655,1 + (9,563 x masa ciała w kilogramach) + (1,85 x wzrost w centymetrach) – (4,676 x wiek w latach)
#dla mężczyzn: PPM = 66,473 + (13,752 x masa ciała w kilogramach) + (5,003 x wzrost w centymetrach) – (6,775 x wiek w latach)
    print("PODAJ PŁEĆ")
    print("1 - mężczyzna")
    print("2 - kobieta")
    
    while True:
        Gender = input()

        # Sprawdzenie czy to liczba
        try:
            Gender = int(Gender)
        except ValueError:
            print("Błąd: Podaj poprawne dane (wybierz 1 lub 2)")
            continue  # Kontynuuj pętlę, aby ponownie zapytać o poprawną wartość

        # Sprawdzenie wyboru płci
        if Gender == 1:
            print("Wybrano płeć mężczyzna")
            return Gender
        elif Gender == 2:
            print("Wybrano płeć kobieta")
            return Gender
        else:
            print("Błąd: Podaj poprawne dane (wybierz 1 lub 2)")
            continue  # Kontynuuj pętlę, aby ponownie zapytać o poprawną wartość

def weight():
    print("Podaj swoją wagę")
    Weight = input()

    try:
        Weight = float(Weight)
        if Weight <= 0:
            print("Podaj prawidłową wagę (wartość powinna być większa od 0)")
            return weight()  # Rekurencyjnie wywołaj funkcję, aby poprosić ponownie o poprawną wagę
        else:
            return Weight  # Zwróć poprawną wagę
    except ValueError:
        print("Błąd: Podaj prawidłową wagę (użyj cyfr)")  # Komunikat o błędzie, jeśli wprowadzono nieprawidłowe dane
        return weight()  # Rekurencyjnie wywołaj funkcję, aby poprosić ponownie o poprawną wagę
    
def hight():
    print("Podaj swój wzrost")
    Hight = input()

    try:
        Hight = float(Hight)
        if Hight <= 0:
            print("Podaj prawidłowy wzrost (wartość powinna być większa od 0)")
            return hight()  # Rekurencyjnie wywołaj funkcję, aby poprosić ponownie o poprawny wzrost
        else:
            return Hight  # Zwróć poprawny wzrost
    except ValueError:
        print("Podaj prawidłowy wzrost (użyj cyfr)")  # Komunikat o błędzie, jeśli wprowadzono nieprawidłowe dane
        return hight()  # Rekurencyjnie wywołaj funkcję, aby poprosić ponownie o poprawny wzrost
    
def age():
    print("Podaj swój wiek")
    Age = input()

    try:
        Age = float(Age)
        if Age <= 0:
            print("Podaj wiek, wartosc musi być większa niż 0")
            return age()  # Rekurencyjnie wywołaj funkcję, aby poprosić ponownie o poprawny wzrost
        else:
            return Age  # Zwróć poprawny wzrost
    except ValueError:
        print("Nieprawidłowe dane podaj swój wiek w liczbach")  # Komunikat o błędzie, jeśli wprowadzono nieprawidłowe dane
        return age()  # Rekurencyjnie wywołaj funkcję, aby poprosić ponownie o poprawny wzrost

def movement():
    print("1 - brak (osoba chora, leżąca w łóżku")
    print("2 - mała (osoba wykonująca pracę siedzącą")
    print("3 - umiarkowana (osoba wykonująca pracę na stojąco")
    print("4 - duża (osoba prowadząca aktywny tryb życia, regularnie ćwicząca")
    print("5 - bardzo duża (osoba prowadząca bardzo aktywny tryb życia, codziennie ćwicząca")
    print("6 - osoba zawodowo uprawiająca sport")
    while True:
        Movement = input()

        # Sprawdzenie czy to liczba
        try:
            Movement = int(Movement)
        except ValueError:
            print("Błąd: Podaj poprawne dane (wybierz 1 lub 2)")
            continue  # Kontynuuj pętlę, aby ponownie zapytać o poprawną wartość

        # Sprawdzenie wyboru płci
        if Movement == 1:
            print("brak (osoba chora, leżąca w łóżku)")
            Activity = float(1.2)
            return Activity
        elif Movement == 2:
            print("mała (osoba wykonująca pracę siedzącą)")
            Activity = float(1.4)
            return Activity
        elif Movement == 3:
            print("umiarkowana (osoba wykonująca pracę na stojąco)")
            Activity = float(1.6)
            return Activity
        elif Movement == 4:
            print("duża (osoba prowadząca aktywny tryb życia, regularnie ćwicząca)")
            Activity = float(1.75)
            return Activity
        elif Movement == 5:
            print("bardzo duża (osoba prowadząca bardzo aktywny tryb życia, codziennie ćwicząca)")
            Activity = float(2)
            return Activity
        elif Movement == 6:
            print("osoba zawodowo uprawiająca sport")
            Activity = float(2.4)
            return Activity
        else:
            print("Błąd: Podaj poprawne dane (wybierz 1 lub 6)")
            continue  # Kontynuuj pętlę, aby ponownie zapytać o poprawną wartość


def CPM():
    #PPM
    #dla kobiet: PPM = 655,1 + (9,563 x masa ciała w kilogramach) + (1,85 x wzrost w centymetrach) – (4,676 x wiek w latach)
    #dla mężczyzn: PPM = 66,473 + (13,752 x masa ciała w kilogramach) + (5,003 x wzrost w centymetrach) – (6,775 x wiek w latach)1
    Gender = gender()
    Weight = weight()
    Hight = hight()
    Age = age()
    Movement = movement()

    if(Gender == 1):
        PPM = 66.473 + (13.752 * Weight) + (5.003 * Hight) - (6.775 * Age)
    else:
        PPM = 655.1 + (9.563 * Weight) + (1.85 * Hight) - (4.676 * Age)
    CPM=PPM*Movement
    print(CPM , "KCAL")
CPM()