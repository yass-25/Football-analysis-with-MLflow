import pandas as pd
import os

def ingest_data():
    # Calcul du chemin absolu vers la racine du projet
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Chemin du fichier d'entrée
    input_path = os.path.join(base_path, 'data', 'raw', 'player_stats.csv')

    # Chemin de sortie
    output_dir = os.path.join(base_path, 'data', 'processed')
    output_path = os.path.join(output_dir, 'ingested.csv')

    # Vérifier que le fichier existe
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Fichier introuvable : {input_path}")

    # Créer le dossier de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)

    # Charger et sauvegarder
    df = pd.read_csv(input_path)
    df.to_csv(output_path, index=False)
    print(f"Données ingérées avec succès : {output_path}")
