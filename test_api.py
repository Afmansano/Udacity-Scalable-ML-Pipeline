from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_post_bellow():
    person = {
        'age': 39,
        'workclass': 'State-gov',
        'fnlgt': 77516,
        'education': 'Bachelors',
        'education_num': 13, 
        'maritial_status': 'Never-married', 
        'ocuupation': 'Adm-clerical', 
        'relationship': 'Not-in-family', 
        'race': 'White', 
        'sex': 'Male', 
        'capital_gain': 2174, 
        'capital_loss': 0, 
        'hours_per_week': 40, 
        'native_country': 'United-States'        
    }
    prediction = client.post("/", json=person)

    assert prediction.status_code == 200
    assert prediction.json()['salary'] == '<=50K'


def test_post_above():
    person = {
        'age': 30,
        'workclass': 'State-gov',
        'fnlgt': 141297,
        'education': 'Bachelors',
        'education_num': 13, 
        'maritial_status': 'Married-civ-spouse', 
        'ocuupation': 'Prof-specialty', 
        'relationship': 'Husband', 
        'race': 'Asian-Pac-Islander', 
        'sex': 'Male', 
        'capital_gain': 0, 
        'capital_loss': 0, 
        'hours_per_week': 40, 
        'native_country': 'India'       
    }
    prediction = client.post("/", json=person)

    assert prediction.status_code == 200
    assert prediction.json()['salary'] == '>50K'


def test_get():
    message = client.get("/")
    assert message.status_code == 200
    assert message.json()['message'] == 'Welcome to ML Pipeline app!'