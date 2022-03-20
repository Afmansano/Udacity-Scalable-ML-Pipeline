"""
Heroku Api test script
"""
import requests

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
r = requests.post('https://afmansanomlpipeline.herokuapp.com/', json=person)
assert r.status_code == 200

print("Response code: %s" % r.status_code)
print("Response body: %s" % r.json())