
# Script to compute scores on slices of data.
import logging 

from sklearn.model_selection import train_test_split

from train_model import read_data
from train_model import get_categorical_features
from train_model import process_data
from train_model import load_model

from ml.model import train_model
from ml.model import inference
from ml.model import compute_model_metrics

from os import path

logging.basicConfig(
    filename='./logs/compute_scores.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

MODEL_FOLDER = "trained_model"


def check_performance_on_slices():
    df = read_data()

    encoder, lb, model = load_model()

    _, test = train_test_split(df, test_size=0.20, random_state=42)
    cat_features = get_categorical_features()

    for feat in cat_features:
        for value in test[feat].unique():
            X_feat = test[test[feat] == value]        
            logging.info(f"Testing on feat {feat} for value {value}")
            X_test, y_test, _, _ = process_data(
            data=X_feat, 
            label="salary", 
            cat_features=cat_features,
            training=False,
            encoder=encoder,
            lb=lb
        )

        y_pred = inference(model, X_test)
        precision, recall, fbeta = compute_model_metrics(y_test, y_pred)

        print(f"Precision on slice {feat}: {precision:.4f}")
        print(f"Recall on slice {feat}: {recall:.4f}")
        print(f"Fbeta on slice {feat}: {fbeta:.4f}\n")
