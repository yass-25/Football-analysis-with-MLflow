import pandas as pd
import os
from sklearn.linear_model import LinearRegression
import pickle

def train_model():
    base_path = os.path.dirname(os.path.abspath(__file__))
    train_path = os.path.join(base_path, '../data/processed/train.csv')
    model_path = os.path.join(base_path, '../models/model.pkl')

    if not os.path.exists(train_path):
        raise FileNotFoundError(f"Fichier introuvable : {train_path}")

    df = pd.read_csv(train_path)

    X = df[['Distance (px)', 'Vitesse moy (px/frame)', 'Temps gauche', 'Temps droite']]
    y = df['Frames']

    model = LinearRegression()
    model.fit(X, y)

    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    print(f"Modèle entraîné et sauvegardé à : {model_path}")
