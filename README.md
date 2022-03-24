# Udacity Scalable ML Pipeline

This project aims to execute a fully CI/CD machine learning devops pipeline. Including model training, tests, deploy on Heroku with Github Actions and models and data versioning with DCV.

## Dependences 

The dependences are listes on file requeriments.txt. They are:

- Python 3.8 or later
- numpy
- pandas
- scikit-learn
- pytest
- requests
- fastapi==0.63.0
- uvicorn
- gunicorn
- dvc
- dvc[s3]

## How to run this code?

- Push data from DVC repository on AWS S3
- To train the model, run: python model/main.py --pipeline_steps train
- To check performance, run: python model/main.py --pipeline_steps check_performance

