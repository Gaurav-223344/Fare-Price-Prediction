# Fare Price Prediction


## Table of Content
  * [Screenshots of Application](#screenshots-of-application)
  * [Teableau Dashboard](#teableau-dashboard)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Technologies Used](#technologies-used)
  * [Team](#team)
  * [Credits](#credits)

## Screenshots of Application
<img target="_blank" src="https://github.com/Gaurav-223344/Fare-Price-Prediction/blob/main/static/img/demo1.png" width=700>

## Teableau Dashboard
Some screnshots of Dashboard

1.  <img target="_blank" src="https://raw.githubusercontent.com/Gaurav-223344/Fare-Price-Prediction/main/static/img/teableau%20flight%20fare%20ss1.png" width=700>

2.  <img target="_blank" src="https://raw.githubusercontent.com/Gaurav-223344/Fare-Price-Prediction/main/static/img/teableau%20flight%20fare%20ss2.png" width=700>


## Overview
This is Flask app for prediction of flight fare. The trained model takes input as Airline, Depature time of flight, Arrival time of flight, Total steps, Source and Destination and predict price of flight.

## Motivation
This is flight fare prediction application to accurately predict price of flight

## Technical Aspect
This project is divided into two part:
1. Training a machine learning model using sklearn. 
2. Building and hosting a Flask web app on Heroku.

## Installation
The Code is written in Python 3.8. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Run
> STEP 1
#### Linux and macOS User
Open `.bashrc` or `.zshrc` file and add the following credentials:
```bash
export AWS_ACCESS_KEY="your_aws_access_key"
export AWS_SECRET_KEY="your_aws_secret_key"
export ICP_BUCKET='your_aws_bucket_name'
export ICP_BUCKET_REGION='bucket_region'
export ICP_UPLOAD_DIR='bucket_path_to_save_images'
export ICP_PRED_DIR='bucket_path_to_save_predictions'
export ICP_FLASK_SECRET_KEY='anything_random_but_unique'
export SENTRY_INIT='URL_given_by_sentry'
```
Note: __SENTRY_INIT__ is optional, only if you want to catch exceptions in the app, else comment/remove the dependencies and code associated with sentry in `app.py`

#### Windows User
Since, I don't have a system with Windows OS, here I collected some helpful resource on adding User Environment Variables in Windows.

__Attention__: Please perform the steps given in these tutorials at your own risk. Please don't mess up with the System Variables. It can potentially damage your PC. __You should know what you're doing__. 
- https://www.tenforums.com/tutorials/121855-edit-user-system-environment-variables-windows.html
- https://www.onmsft.com/how-to/how-to-set-an-environment-variable-in-windows-10

> STEP 2

To run the app in a local machine, shoot this command in the project directory:
```bash
gunicorn wsgi:app
```

## Deployement on Heroku
Set the environment variable on Heroku as mentioned in _STEP 1_ in the __Run__ section. [[Reference](https://devcenter.heroku.com/articles/config-vars)]

![](https://i.imgur.com/TmSNhYG.png)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
├── app.py
├── templates
│   └── index.html
├── static
│   └── img
│       ├── img.jpg
│       └── demo.jpg
├── flight_rf_1.pkl
├── .gitattributes.txt
├── Fare prediction.ipynb
├── Data_Train.csv
├── Test_set.csv
├── requirements.txt
├── Procfile
└── README.md

```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) [<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) 

## Team
[Gaurav-Gaikwad](https://github.com/Gaurav-223344)


## Credits
- [Airlines Fare Prediction Dataset(Kaggle)](https://www.kaggle.com/absin7/airlines-fare-prediction) - This project wouldn't have been possible without this dataset. It saved my enormous amount of time while collecting the data. Also huge shout-out to [Krish-Naik](https://github.com/krishnaik06) and [Amar Mandal](https://github.com/Mandal-21)
