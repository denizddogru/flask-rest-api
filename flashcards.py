from datetime import datetime

from flask import Flask

# export FLASK_APP=flashcards.py
# location of modulencontaining our aplication
#
# export FLASK_DEV=development
# runs the program in debug mode, enables development features
# flask run
# flask maps urls to views functions


app = Flask(__name__)
# flask object called name stored in the variable called app.

@app.route("/")
def welcome():
    return "Welcome to my Flash cards application."

@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())


counter = 0

@app.route("/count_views")
def count_views():
    global counter
    counter += 1
    return "This page was served " + str(counter) + " times."