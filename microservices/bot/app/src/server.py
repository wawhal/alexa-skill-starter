from src import app
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode


ask = Ask(app, "/reddit_reader")

def getYodaQuote():
	url = http://data.hasura/v1/query
	headers = {
		"Content-type": "application/json"
	}
	body = {}

@app.route('/')
def homepage():
    return "Alexa skill is running."

@ask.launch
def startSkill():
    welcome_message = 'Hello there, would you like the news?'
    return question(welcome_message)

@ask.intent("YesIntent")
def shareQuote():
    quote = getYodaQuote()
    headline_msg = 'The current world news headlines are... '+quote
    return statement(headline_msg)

@ask.intent("NoIntent")
def noIntent():
    bye_text = 'I am not sure why you asked me to run then, but okay... bye'
    return statement(bye_text)

