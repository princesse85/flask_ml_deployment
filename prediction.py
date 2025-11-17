import joblib


def predict(data):
    loaded_model = joblib.load('temperature_model.joblib')
    return loaded_model.predict(data)
