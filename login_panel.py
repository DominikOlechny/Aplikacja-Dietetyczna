import pandas as pd

def login_user():
    # Wczytaj dane z pliku CSV
    path_users_info = 'users_info.csv'
    users = pd.read_csv(path_users_info, delimiter=';')
    while True:
        username = input("Podaj login: ")
        password = input("Podaj hasło: ")

        user = users[(users['Login'] == username) & (users['Password'] == password)]

        if not user.empty:
            print(f"Witaj, {username}!")
            log_user = user.iloc[0]  # Pobieramy pierwszego użytkownika, który pasuje do loginu i hasła
            
            # Przypisywanie danych użytkownika do zmiennych
            login = log_user['Login']
            cpm = log_user['CPM']
            protein = log_user['Protein']
            fats = log_user['Fats']
            carbs = log_user['Carbs']
            total_cpm = log_user['Total_cpm']
            total_carbs = log_user['Total_carbs']
            total_pal = log_user['Total_pal']
            total_fats = log_user['Total_fats']
            return login, cpm, protein, fats, carbs, total_cpm, total_carbs, total_pal, total_fats
        else:
            print("Niepoprawne dane logowania. Spróbuj ponownie.")

