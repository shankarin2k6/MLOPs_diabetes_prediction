import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def run_experiment():
    mlflow.set_experiment("Diabetes_Project")
    with mlflow.start_run():
        data = load_diabetes()
        X = pd.DataFrame(data.data, columns=data.feature_names)
        y = data.target
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        model = RandomForestRegressor(n_estimators=100)
        model.fit(X_train, y_train)
        
        # Log parameters and model
        mlflow.log_param("model_type", "RandomForest")
        mlflow.sklearn.log_model(model, "model")
        print("Experiment Complete. Model logged to MLflow.")

if __name__ == "__main__":
    run_experiment()