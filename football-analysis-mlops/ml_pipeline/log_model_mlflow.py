import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn

def log_model_to_mlflow():
    # Chemins absolus
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, "../data/processed")

    X_train = pd.read_csv(os.path.join(data_path, "X_train.csv"))
    X_test = pd.read_csv(os.path.join(data_path, "X_test.csv"))
    y_train = pd.read_csv(os.path.join(data_path, "y_train.csv")).values.ravel()
    y_test = pd.read_csv(os.path.join(data_path, "y_test.csv")).values.ravel()

    # Config MLflow
    mlflow.set_tracking_uri("file:///tmp/mlruns")
    mlflow.set_experiment("Football Analysis")

    # Stop any active run
    if mlflow.active_run():
        mlflow.end_run()

    with mlflow.start_run():
        # Modèle
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Log des hyperparamètres
        for param, value in model.get_params().items():
            mlflow.log_param(param, value)

        # Prédictions & métrique
        y_pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mlflow.log_metric("rmse", rmse)

        # Enregistrement du modèle
        mlflow.sklearn.log_model(model, artifact_path="model")

        print("✅ Modèle loggé avec succès dans MLflow.")