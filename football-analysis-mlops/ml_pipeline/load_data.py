import pandas as pd
import os

def load_data():
    """
    Fonction d’ingestion des données. Elle lit un fichier CSV brut
    et le sauvegarde dans le dossier temporaire du pipeline.
    """
    # Remplace ce chemin par le vrai chemin vers ton fichier de données
    input_path = "data/raw/players_stats.csv"
    output_path = "data/processed/loaded_data.csv"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Chargement des données
    df = pd.read_csv(input_path)

    # Sauvegarde dans un format propre pour la suite du pipeline
    df.to_csv(output_path, index=False)
    print(f"[load_data] Données chargées et sauvegardées dans {output_path}")

