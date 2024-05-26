from login_panel import login_user
from addup_calories import choose_produts, view_nutriens
from add_info import info

def main_menu():
    login = login_user()  # Pobierz login użytkownika po zalogowaniu
    while True:
        print("Główne Menu")
        print("1. Oblicz swoje zapotrzebowanie kaloryczne")
        print("2. Oblicz swój koszyk zakupów")
        print("3. Wyjście")
        
        choice = input("Wybierz opcję (1-3): ")
        
        if choice == '1':
            print("Wprowadź informację o sobie")
            info(login)
        elif choice == '2':
            print("Oblicz swój koszyk zakupów")
            view_nutriens()
        elif choice == '3':
            print("Dziękujemy za skorzystanie z menu. Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main_menu()