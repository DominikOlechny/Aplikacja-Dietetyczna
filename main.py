from addup_calories import choose_produts, view_nutriens
from add_info import info


def main_menu():
    while True:
        print("Główne Menu")
        print("1. Oblicz swoje zapotrzebowanie kaloryczne")
        print("2. Oblicz swój koszyk zakupów")
        print("Wyjście")
        
        choice = input("Wybierz opcję (1-3): ")
        
        if choice == '1':
            print("Wybrałeś Oblicz swoje zapotrzebowanie kaloryczne")
            choose_produts()
        elif choice == '2':
            print("Oblicz swój koszyk zakupów")
            view_nutriens()
        elif choice == '3':
            print("Oblicz swój koszyk zakupów")
            info()
        elif choice == '4':
            print("Dziękujemy za skorzystanie z menu. Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

main_menu()