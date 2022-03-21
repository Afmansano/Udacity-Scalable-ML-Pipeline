import logging

from sklearn.metrics import fbeta_score, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

from os import path
from os import mkdir


logging_path = './model/logs/'
if not path.exists(logging_path):
    mkdir(logging_path)

logging.basicConfig(
    filename=path.join(logging_path, 'model.log'),
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Optional: implement hyperparameter tuning.
def train_model(X_train, y_train):
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """

    rf = RandomForestClassifier()

    # Defines a GridSearch for hyperparameter tunning 
    # that maximises f1
    params = {
        'n_estimators': [100, 150, 200]
    }
    clf = GridSearchCV(
        estimator=rf, 
        param_grid=params,
        scoring='f1'
    )

    logger.info("Fitting classifier")
    clf.fit(X_train, y_train)
    model = clf.best_estimator_

    logger.info(f"Parameters = {clf.best_params_} F1 = {clf.best_score_}")
    
    return model
    
    

def compute_model_metrics(y, preds):
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """

    logger.info("Computting metrics")
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, fbeta


def inference(model, X):
    """ Run model inferences and return the predictions.

    Inputs
    ------
    model : Random Forest Model
        Trained machine learning model.
    X : np.array
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    preds = model.predict(X)
    return preds
