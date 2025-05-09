# Football Analysis MLOps Pipeline

Ce projet implémente un pipeline complet de Machine Learning dans le cadre d’un projet de fin d’études, en utilisant **Apache Airflow** pour l’orchestration et **MLflow** pour le suivi des expériences.

## Objectifs

- Automatiser les étapes d’un workflow ML :
  - Ingestion des données
  - Prétraitement
  - Split train/test
  - Entraînement d’un modèle de régression
  - Suivi des métriques et versionnement du modèle avec MLflow

## Structure du projet

```
football-analysis-mlops/
│
├── dags/
│   └── football_pipeline.py     # Pipeline Airflow (DAG)
│
├── ml_pipeline/
│   ├── ingest_data.py
│   ├── preprocess.py
│   ├── split_data.py
│   ├── train_model.py
│   └── log_model_mlflow.py
│
├── data/
│   ├── raw/                     # Fichier CSV d’origine
│   └── processed/               # Données transformées et fichiers de split
│
└── README.md
```

## Lancer le pipeline

### 1. Prérequis

- Python 3.9+
- Apache Airflow
- MLflow
- Pandas, Scikit-learn, NumPy

Installe les dépendances :

```bash
pip install -r requirements.txt
```

### 2. Lancer Airflow

```bash
export AIRFLOW_HOME=~/airflow
airflow db init
airflow webserver --port 8080
airflow scheduler
```

Accéder à l’interface : http://localhost:8080

Lancer manuellement le DAG `football_analysis_pipeline`.

### 3. Lancer l’interface MLflow

```bash
mlflow ui --backend-store-uri file:///tmp/mlruns --port 5000
```

Accéder à l’interface : http://localhost:5000

### 4. Fichier source attendu

Le fichier d’entrée attendu doit être placé dans :
```
data/raw/player_stats.csv
```

Format :
```
Joueur,Distance (px),Vitesse moy (px/frame),Temps gauche,Temps droite,Frames
1,438.03,1.3,336,0,336
...
```

## Résultats

- Les métriques de performance (RMSE)
- Les hyperparamètres du modèle
- Le modèle sauvegardé

Tous ces éléments sont visibles dans l’interface MLflow.

---

## Auteur

Projet réalisé dans le cadre du PFE MAIA à Télécom SudParis.