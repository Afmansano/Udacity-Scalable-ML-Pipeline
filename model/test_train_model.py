# this module implements unit tests for the project

import logging
from os import path

from .train_model import read_data
from .train_model import get_categorical_features
from .train_model import process_data
from .train_model import train
from .train_model import load_model

from .ml.model import inference

logging.basicConfig(
    filename='./logs/tests.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

MODEL_FOLDER = "../trained_model"


def test_read_data():
    '''
    test data load
    '''

    try:
        df = read_data()
        logging.info("SUCCESS: Testing read_data")
    except FileNotFoundError as err:
        logging.error("Testing read_data: The file wasn't found")
        raise err

    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0
    except AssertionError as err:
        logging.error(
            "Testing import_data: The file doesn't appear to \
                have rows and columns")
        raise err


def test_process_data():
    '''
    test data processing and encoders
    '''

    df = read_data()[:1000]

    try:
        X, y, encoder, lb = process_data(
            df, 
            label="salary",
            cat_features=get_categorical_features(),
            training=True
        )
        assert encoder is not None and lb is not None
    except AssertionError as err:
        logging.error(
            "Testing process_data: created encoders should be not \
                be None for training")
        raise err

    try:
        assert X.shape[0] > 0
        assert X.shape[1] > 0
    except AssertionError as err:
        logging.error(
            "Testing process_data: The X dataframe doesn't appear to \
                have rows and columns")
        raise err

    try:
        assert y is not None and len(y) > 0
    except AssertionError as err:
        logging.error("Testing process_data: y should not be 0-dimension")
        raise err

    
def test_train():
    '''
    test model train pipeline and if it saves on disk
    '''

    try:
        train()
        assert path.isfile(path.join(MODEL_FOLDER, "model.pkl"))
        assert path.isfile(path.join(MODEL_FOLDER, "categorical_encoder.pkl"))
        assert path.isfile(path.join(MODEL_FOLDER, "label_encoder.pkl"))
    except AssertionError as err:
        logging.error("Testing train: model not saved")
        raise err


def test_load_model():
    '''
    test model and encoder loading
    '''

    try:
        encoder, lb, model = load_model()
        assert encoder is not None
        assert lb is not None
        assert model is not None
    except AssertionError as err: 
        logging.error(
            "Seriliazed model components not loaded"
        )
        raise err


def test_inference():
    '''
    test model inference
    '''
    df = read_data()[:100]

    #perform test with no label
    df = df.drop(['salary'], axis=1)
    encoder, lb, model = load_model()

    try:
        X, _, _, _ = process_data(
            data=df, 
            label=None, 
            cat_features=get_categorical_features(),
            training=False,
            encoder=encoder,
            lb=lb
        )
        preds = inference(model, X)
        assert preds is not None
    except AssertionError as err:
        logging.error("Testing inference: model returned None")
        raise err

    try:
        assert len(preds) == X.shape[0]
    except AssertionError as err:
        logging.error(
            "Testing inference: model prediction length is different of X instances length")
        raise err