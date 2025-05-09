import os
import pandas as pd
from sklearn.model_selection import train_test_split

def split_data():
    # Déterminer le chemin absolu du fichier
    base_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_path, '../data/processed/preprocessed.csv')

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Fichier introuvable : {input_path}")

    # Lire les données prétraitées
    df = pd.read_csv(input_path)

    # Séparer les variables indépendantes (X) et la cible (y)
    X = df.drop(columns=['Vitesse moy (px/frame)'])
    y = df['Vitesse moy (px/frame)']

    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Chemin de sauvegarde
    output_dir = os.path.join(base_path, '../data/processed')

    # Sauvegarder les fichiers
    X_train.to_csv(os.path.join(output_dir, 'X_train.csv'), index=False)
    X_test.to_csv(os.path.join(output_dir, 'X_test.csv'), index=False)
    y_train.to_csv(os.path.join(output_dir, 'y_train.csv'), index=False)
    y_test.to_csv(os.path.join(output_dir, 'y_test.csv'), index=False)

    print("✅ Données sauvegardées après split dans :", output_dir)
