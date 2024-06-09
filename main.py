#menu bglowne

from login_panel import readCSV, login_user
from addup_calories import choose_produts, view_nutriens, save_totals
from add_info import info
from generate_chart import generate_macro_chart



def main_menu(): #funckja odpowiedzialna za główne menu wyswietlane po zalogowaniu
    path_users_info = 'users_info.csv' #sciezka do pliku z userami
    users = readCSV() #pobranie danych z funkcji oddczytujacej csv
    login, cpm, protein, fats, carbs, total_cpm, total_carbs, total_pal, total_fats = login_user(users) #przypisanie informacji o userze
    while True: #petla wykonuje sie do spelnienienia warunku tzn, do momentu wyjscia z programu lub wybrania opcji
        #wizualna reprezentacja menu
        print("Główne Menu") 
        print("1. Oblicz swoje zapotrzebowanie kaloryczne")
        print("2. Oblicz swój koszyk zakupów")
        print("3. Zobacz wykres spełnienia makroskładników")
        print("4. Wyjście")
        choice = input("Wybierz opcję (1-4): ") 
        if choice == '1': #uruchamia sie opcja edycji obliczania makroskladnikow dla zalogowanego uzytkownika
            print("Wprowadź informację o sobie") 
            info(login, path_users_info)
        elif choice == '2': #uruchamia sie opcja tworzenia produktu
            print("Oblicz swój koszyk zakupów")
            choose_produts()
            totals = view_nutriens() #zapis do pliku csv uzytkownika
            save_totals(totals, login) #cd
        elif choice == '3': #generowanie wykresu
            print("Generowanie wykresu spełnienia makroskładników") 
            generate_macro_chart(login) 
        elif choice == '4':
            print("Dziękujemy za skorzystanie z menu. Do widzenia!") #wyjscie z programu
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.") #zly wybor ponowny wywolanie petli menu 

main_menu()