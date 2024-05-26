#Dane do CSV POBIERANE Z STĄD https://cloud-d.edupage.org/cloud/TABELA_WARTOSCI_ODZYWCZYCH.pdf?z%3APDDb3bKBXlY%2FWjIPy4GrEnwqpQPbkRKS5bz%2B61bSkv9GuOPTeTEfb6uDNr0VpRuj

import pandas as pd
from login_panel import readCSV, login_user

# Wczytaj dane z pliku CSV
file_path = 'nutrition_table.csv'
df = pd.read_csv(file_path, delimiter=';')

# Funkcja do wyszukiwania produktów na podstawie fragmentu nazwy
def find_products(fragment):
    return df[df['Nazwa'].str.contains(fragment, case=False)]

def select_product(product_name, selected_products):
    matching_products = find_products(product_name)
    if len(matching_products) == 0:
        print(f'Produkt "{product_name}" nie został znaleziony.')
    elif len(matching_products) == 1:
        selected_products.append(matching_products.iloc[0])
        print(f'Produkt "{matching_products.iloc[0]["Nazwa"]}" został dodany.')
    else:
        print(f'Znaleziono kilka produktów pasujących do "{product_name}":')
        for i, row in matching_products.iterrows():
            print(f'- {row["Nazwa"]}')
        choice = input("Wybierz nazwę produktu: ")
        if choice in matching_products['Nazwa'].values:
            selected_products.append(matching_products[matching_products['Nazwa'] == choice].iloc[0])
            print(f'Produkt "{choice}" został dodany.')
        else:
            print("Niepoprawny wybór.")

# Funkcja do sumowania wartości odżywczych
def calculate_totals(selected_products):
    total_cpm = 0
    total_carbs = 0
    total_pal = 0
    total_fats = 0
    
    for product in selected_products:
        total_cpm += product['KCAL']
        total_carbs += product['WEGLOWODANY']
        total_pal += product['BIALKO']
        total_fats += product['TLUSZCZ']
    
    return {
        "KCAL": total_cpm,
        "WEGLOWODANY": total_carbs,
        "BIALKO": total_pal,
        "TLUSZCZ": total_fats
    }
# Lista na wybrane produkty
selected_products = []

def choose_produts():
    while True:
        product = input("Podaj nazwę produktu, który chcesz dodać do listy (wpisz 'stop', aby zakończyć): ")
        if product.lower() == "stop":
            break
        else:
            select_product(product, selected_products)

def view_nutriens():
    totals = calculate_totals(selected_products)
    print("Suma wartości odżywczych dla wybranych produktów:")
    print(f'Kalorie: {totals["KCAL"]}')
    print(f'Węglowodany: {totals["WEGLOWODANY"]}')
    print(f'Białko: {totals["BIALKO"]}')
    print(f'Tłuszcz: {totals["TLUSZCZ"]}')
    return totals

def save_totals(totals, login):
    path_users_info = 'users_info.csv'
    users = pd.read_csv(path_users_info, delimiter=';')
    
    users.loc[users['Login'] == login, 'Total_cpm'] = totals["KCAL"]
    users.loc[users['Login'] == login, 'Total_carbs'] = totals["WEGLOWODANY"]
    users.loc[users['Login'] == login, 'Total_pal'] = totals["BIALKO"]
    users.loc[users['Login'] == login, 'Total_fats'] = totals["TLUSZCZ"]
    
    users.to_csv(path_users_info, sep=';', index=False)
    print("Wartości odżywcze zostały zapisane do pliku CSV.")
