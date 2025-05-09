import os
import pandas as pd

def preprocess_data():
    base_path = os.path.dirname(os.path.abspath(__file__))  # chemin absolu
    input_path = os.path.join(base_path, '../data/processed/ingested.csv')
    output_path = os.path.join(base_path, '../data/processed/preprocessed.csv')

    df = pd.read_csv(input_path)
    
    # Exemple simple de preprocessing
    df = df.dropna()  # Nettoyage de base
    df.to_csv(output_path, index=False)


    # Vérification des colonnes attendues
    expected_columns = {'Distance (px)', 'Vitesse moy (px/frame)', 'Temps gauche', 'Temps droite', 'Frames'}
    if not expected_columns.issubset(df.columns):
        raise ValueError(f"Colonnes manquantes. Colonnes attendues : {expected_columns}")

    # Exemple de normalisation simple des colonnes numériques
    df[['Distance (px)', 'Vitesse moy (px/frame)']] = df[['Distance (px)', 'Vitesse moy (px/frame)']].apply(
        lambda x: (x - x.mean()) / x.std()
    )

    # Sauvegarde des données prétraitées
    df.to_csv(output_path, index=False)
