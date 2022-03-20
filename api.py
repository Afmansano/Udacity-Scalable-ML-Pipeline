import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel

from model.train_model import load_model
from model.train_model import process_data
from model.train_model import get_categorical_features
from model.ml.model import inference

#age,workclass,fnlgt,education,education-num,marital-status,occupation,relationship,race,sex,capital-gain,capital-loss,hours-per-week,native-country,salary


class Person(BaseModel):
    age: int
    workclass: str
    fnlgt: int
    education: str
    education_num: int 
    maritial_status: str 
    ocuupation: str 
    relationship: str 
    race: str 
    sex: str 
    capital_gain: int 
    capital_loss: int 
    hours_per_week: int 
    native_country: str 


app = FastAPI()

@app.post("/")
async def predict(person: Person):

    data = pd.DataFrame({
        'age': person.age,
        'workclass': person.workclass,
        'fnlgt': person.fnlgt,
        'education': person.education,
        'education-num': person.education_num,
        'marital-status': person.maritial_status,
        'occupation': person.ocuupation,
        'relationship': person.relationship,
        'race': person.race,
        'sex': person.sex,
        'capital-gain': person.capital_gain,
        'capital-loss': person.capital_loss,
        'hours-per-week': person.hours_per_week,
        'native-country': person.native_country
    }, index=[0])

    encoder, lb, model = load_model('model/trained_model')

    X, _, _, _ = process_data(
        data=data, 
        label=None, 
        cat_features=get_categorical_features(),
        lb=lb,
        encoder=encoder,
        training=False
    )
    
    pred = inference(model, X)
    salary = lb.inverse_transform(pred)[0]
    return {
        "salary" : salary
    }

@app.get("/")
async def send_message():
    return {
        "message": "Welcome to ML Pipeline app!"
    }




    
