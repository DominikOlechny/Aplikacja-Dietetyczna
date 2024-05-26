from login_panel import readCSV, login_user
from addup_calories import choose_produts, view_nutriens, save_totals
from add_info import info



def main_menu():
    path_users_info = 'users_info.csv'
    users = readCSV()
    login, cpm, protein, fats, carbs, total_cpm, total_carbs, total_pal, total_fats = login_user(users)
    while True:
        print("Główne Menu")
        print("1. Oblicz swoje zapotrzebowanie kaloryczne")
        print("2. Oblicz swój koszyk zakupów")
        print("3. Wyjście")
        
        choice = input("Wybierz opcję (1-3): ")
        
        if choice == '1':
            print("Wprowadź informację o sobie")
            info(login, path_users_info)
        elif choice == '2':
            print("Oblicz swój koszyk zakupów")
            choose_produts()
            totals = view_nutriens()
            save_totals(totals, login)
        elif choice == '3':
            print("Dziękujemy za skorzystanie z menu. Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")