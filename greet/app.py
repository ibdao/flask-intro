from flask import Flask
app = Flask(__name__)


@app.get('/welcome')
def say_welcome():
    """Says Welcome"""
    greeting = "<html><body><h1>Welcome</h1></body></html>"
    return greeting

PLACES = {"home": "home", "back": "back"}

@app.get('/welcome/<place>')
def go_home(place):
    """Says Welcome 'destination' """
    place = PLACES[place]
    welcome_place = f"<html><body><h1>Welcome {place}!</h1></body></html>"
    return welcome_place