# Script to train machine learning model.
import pandas as pd
import numpy as np
import logging

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import OneHotEncoder
from joblib import dump
from joblib import load
from model.ml.model import train_model
from os import path
from os import mkdir

logging_path = './model/logs/'
if not path.exists(logging_path):
    mkdir(logging_path)

logging.basicConfig(
    filename=path.join(logging_path,'train_model.log'),
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

MODEL_FOLDER = "trained_model"


def get_categorical_features():
    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]
    return cat_features


def process_data(
    data, 
    label, 
    cat_features, 
    training=True, 
    encoder=None, 
    lb=None
):
    """
    Process data for training or inference

    Inputs
    ------
    data: pd.DataFrame
        Raw Data
    label: str
        Name of the label column in data
    training: bool
        Flag for training or inference
    encoder: sklearn.preprocessing.OneHotEncoder, None
        Encoder to be applied on categorical data. Not Required for training,
        but Required for inference 
    lb: sklearn.preprocessing.LabelBinarizer, None
        Label Encoder to be fitted on training data. Not Required for training, 
        but Required for inference

    Returns
    -------
    X: np.array
        Numpy array with processed features
    y: np.array
        Numpy array with binarized labels
    encoder: sklearn.preprocessing.OneHotEncoder
        One Hot Encoder fitted on training data
    lb: sklearn.preprocessing.LabelBinarizer
        Label Binarizer fitted on training dara
    """

    if label is not None:
        y = data[label]
        X = data.drop([label], axis=1)
    else:
        y = None
        X = data

    logger.info("Getting categorical features")
    X_cat = X[cat_features]
    X_num = X.drop(*[cat_features], axis=1)

    if training:
        logger.info("Fitting encoders")
        lb = LabelBinarizer().fit(y.values)
        encoder = OneHotEncoder(
            sparse=False, 
            handle_unknown="ignore"
        ).fit(X_cat.values)
    else:
        logger.info("Performing inference")
    
    logger.info("Transforming encoders")

    if label is not None:
        y = lb.transform(y.values).ravel()
    
    X_cat = encoder.transform(X_cat.values)
    X = np.concatenate([X_cat, X_num], axis=1)
    return X, y, encoder, lb 


def read_data():
    """
    Loads census data
    """
    # Add code to load in the data.
    df = pd.read_csv("data/clean_census.csv")
    return df


def train(model_folder=MODEL_FOLDER):
    """
    Trains a machine learning model and saves its artifacts

    Inputs
    ---------
    model_folder: str
        Path to the folder where the model will be saved
    """
    df = read_data()

    # Optional enhancement, use K-fold cross validation 
    # instead of a train-test split.
    train, test = train_test_split(df, test_size=0.20, random_state=42) 
    cat_features = get_categorical_features()

    X_train, y_train, encoder, lb = process_data(
        train,
        label="salary",
        cat_features=cat_features,
        training=True
    )

    # Proces the test data with the process_data function.
    X_test, y_test, _, _ = process_data(
        test, 
        label="salary", 
        cat_features=cat_features,
        training=False,
        encoder=encoder, 
        lb=lb
    )

    # Train and save a model.
    if not path.exists(model_folder):
        mkdir(model_folder)

    model = train_model(X_train, y_train)

    if not path.exists(model_folder):
        mkdir(model_folder)

    dump(model, path.join(model_folder, "model.pkl"))
    dump(encoder, path.join(model_folder, "categorical_encoder.pkl"))
    dump(lb, path.join(model_folder, "label_encoder.pkl"))


def load_model(model_folder=MODEL_FOLDER):
    """
    Loads a trained machine learning model artifacts

    Inputs
    --------
    model_folder: str
        Path to the folder where the models artifacts are saved
    """
    logging.info("Loading model")
    model = load(path.join(model_folder, "model.pkl"))

    logging.info("Loading label encoder")
    lb = load(path.join(model_folder, "label_encoder.pkl"))

    logging.info("Loading categorical encoder")
    encoder = load(path.join(model_folder, "categorical_encoder.pkl"))

    return encoder, lb, model