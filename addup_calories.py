#Dane do CSV POBIERANE Z STĄD https://cloud-d.edupage.org/cloud/TABELA_WARTOSCI_ODZYWCZYCH.pdf?z%3APDDb3bKBXlY%2FWjIPy4GrEnwqpQPbkRKS5bz%2B61bSkv9GuOPTeTEfb6uDNr0VpRuj

import pandas as pd

# Wczytaj dane z pliku CSV
file_path = 'nutrition_table.csv'
df = pd.read_csv(file_path, delimiter=';')

# Funkcja do interaktywnego wybierania produktów
def select_product(product_name, selected_products):
    product = df[df['Nazwa'] == product_name]
    if not product.empty:
        selected_products.append(product)
        print(f'Produkt "{product_name}" został dodany.')
    else:
        print(f'Produkt "{product_name}" nie został znaleziony.')

# Funkcja do sumowania wartości odżywczych
def calculate_totals(selected_products):
    total_kcal = 0
    total_weglowodany = 0
    total_bialko = 0
    total_tluszcz = 0
    
    for product in selected_products:
        total_kcal += product['KCAL'].values[0]
        total_weglowodany += product['WEGLOWODANY'].values[0]
        total_bialko += product['BIALKO'].values[0]
        total_tluszcz += product['TLUSZCZ'].values[0]
    
    return {
        "KCAL": total_kcal,
        "WEGLOWODANY": total_weglowodany,
        "BIALKO": total_bialko,
        "TLUSZCZ": total_tluszcz
    }

# Lista na wybrane produkty
selected_products = []

# Przykładowe użycie
select_product("Indyk, mieso z piersi bez skory", selected_products)
select_product("Indyk, mieso z udzca ze skora", selected_products)

# Obliczanie sum
totals = calculate_totals(selected_products)
print("Suma wartości odżywczych dla wybranych produktów:")
print(f'Kalorie: {totals["KCAL"]}')
print(f'Węglowodany: {totals["WEGLOWODANY"]}')
print(f'Białko: {totals["BIALKO"]}')
print(f'Tłuszcz: {totals["TLUSZCZ"]}')