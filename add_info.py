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
import pandas as pd
from login_panel import login_user

path_users_info = 'users_info.csv'
users = pd.read_csv(path_users_info, delimiter=';')

def get_gender():


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

def get_weight():
    while True:
        try:
            Weight = float(input("Podaj swoją wagę: "))
            if Weight > 0:
                return Weight  # Zwróć poprawną wagę
            else:
                print("Podaj prawidłową wagę (wartość powinna być większa od 0)")
        except ValueError:
            print("Błąd: Podaj prawidłową wagę (użyj cyfr)")  # Komunikat o błędzie, jeśli wprowadzono nieprawidłowe dane

    
def get_height():
    while True:
        try:
            Height = float(input("Podaj swój wzrost: "))
            if Height > 0:
                return Height  # Zwróć poprawny wzrost
            else:
                print("Podaj prawidłowy wzrost (wartość powinna być większa od 0)")
        except ValueError:
            print("Podaj prawidłowy wzrost (użyj cyfr)")  # Komunikat o błędzie, jeśli wprowadzono nieprawidłowe dane
    
def get_age():
    while True:
        try:
            Age = int(input("Podaj swój wiek: "))
            if Age > 0:
                return Age  # Zwróć poprawny wiek
            else:
                print("Podaj wiek, wartość musi być większa niż 0")
        except ValueError:
            print("Nieprawidłowe dane podaj swój wiek w liczbach")  # Komunikat o błędzie, jeśli wprowadzono nieprawidłowe dane

def get_movement():
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
            print("Błąd: Podaj poprawne dane (wybierz 1 lub 6)")
            continue  # Kontynuuj pętlę, aby ponownie zapytać o poprawną wartość

        # Sprawdzenie aktywnosci
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


def get_CPM(gender, weight, hight, age, activity):
    #PPM przemiana materii
    #dla kobiet: PPM = 655,1 + (9,563 x masa ciała w kilogramach) + (1,85 x wzrost w centymetrach) – (4,676 x wiek w latach)
    #dla mężczyzn: PPM = 66,473 + (13,752 x masa ciała w kilogramach) + (5,003 x wzrost w centymetrach) – (6,775 x wiek w latach)1
   
    if(gender == 1):
        PPM = 66.473 + (13.752 * weight) + (5.003 * hight) - (6.775 * age)
    else:
        PPM = 655.1 + (9.563 * weight) + (1.85 * hight) - (4.676 * age)
    CPM=PPM*activity
    return CPM #ilosc kilokalorii

def get_PAL(weight, activity): #Dzienne zapotrzebowanie na białko
    pal_factors = {
        1.2: 1.2, 1.4: 1.3, 1.6: 1.4, 1.75: 1.5, 2.0: 1.7, 2.4: 2.0
    }
    protein_requirement = pal_factors[activity] * weight
    return protein_requirement

def get_fats(CPM): #Dzienne zapotrzebowanie na tłuszcz
    fats = (CPM - (CPM * 0.75)) / 9
    return fats

def get_carbs(CPM):
    carbs = CPM*0.5/4 #ze wzoru kcal*50%/4
    return carbs

def info(login, users):
    users = pd.read_csv(path_users_info, delimiter=';')
    
    gender = get_gender()
    weight = get_weight()
    height = get_height()
    age = get_age()
    activity = get_movement()

    CPM = get_CPM(gender, weight, height, age, activity)
    protein_requirement = get_PAL(weight, activity)
    fats = get_fats(CPM)
    carbs = get_carbs(CPM)