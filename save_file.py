import os
import pandas as pd
from datetime import datetime

# Fonction pour générer un nom de fichier unique
def generate_filename(base_name, extension):
    counter = 0
    while True:
        if counter == 0:
            file_name = f"{base_name}.{extension}"
        else:
            file_name = f"{base_name}_{counter}.{extension}"
        
        if not os.path.exists(file_name):
            return file_name
        counter += 1

# Lecture des fichiers Excel d'un dossier et création d'un DataFrame combiné
def read_excel_files(folder_path):
    all_data = pd.DataFrame()
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".xlsx"):
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_excel(file_path)
            all_data = pd.concat([all_data, df], ignore_index=True)
    return all_data

# Fonction principale pour lire, combiner et sauvegarder le DataFrame
def save_combined_excel(folder_path):
    today = datetime.today().strftime('%Y-%m-%d')  # Date du jour
    base_name = f"portfolio_analysis_{today}"
    extension = "xlsx"

    # Générer un nom de fichier unique
    file_name = generate_filename(base_name, extension)
    
    # Lire et combiner les fichiers Excel
    combined_data = read_excel_files(folder_path)
    
    # Sauvegarder le DataFrame dans le fichier Excel
    combined_data.to_excel(file_name, index=False)
    print(f"DataFrame saved as: {file_name}")

# Exemple d'utilisation
folder_path = "chemin/vers/votre/dossier"  # Remplacez par le chemin de votre dossier
save_combined_excel(folder_path)