# Flight Fare Prediction


## Table of Content
   * [Screenshots of Application](#screenshots-of-application)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Technologies Used](#technologies-used)
  * [Contributor](#contributor)
  * [TODO](#todo)
  * [Acknowledgements](#acknowledgements)

## Screenshots of Application

<img target="_blank" src="https://github.com/Gaurav-223344/Fare-Price-Prediction/blob/main/static/img/demo1.png" width=700>

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

#### Linux and macOS User
Open terminal :
```bash
$ python3 app.py
```
This sources will help you to run this project:\
for macOS user : https://www.maketecheasier.com/run-python-script-in-mac \
for Linux user : https://www.educative.io/edpresso/how-to-run-a-python-script-in-linux

#### Windows User
Open Command Prompt :
```bash
$ python3 app.py
```
This will help you if you are windows user and also a beginner :
https://github.com/pettarin/python-on-windows

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

## Contributor
[Gaurav-Gaikwad](https://github.com/Gaurav-223344)

## TODO

#### Better FrontEnd

## Acknowledgements
- [Airlines Fare Prediction Dataset(Kaggle)](https://www.kaggle.com/absin7/airlines-fare-prediction) - This project wouldn't have been possible without this dataset. It saved my enormous amount of time while collecting the data. Also huge shout-out to [Krish-Naik](https://github.com/krishnaik06) and [Amar Mandal](https://github.com/Mandal-21)
