from src import app
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode
import random


ask = Ask(app, "/reddit_reader")

def getYodaQuote():
	url = "http://data.hasura/v1/query"
	headers = {
		"Content-type": "application/json"
	}
	body = {
	    "type": "run_sql",
	    "args": {
	        "sql": "SELECT quote FROM yoda_quotes ORDER BY RANDOM() limit 1;"
	    }
	}
	response = requests.request("POST", url, data=json.dumps(body), headers=headers)
	respObj = response.json()
	return respObj[0]


@app.route('/')
def homepage():
    return "Alexa skill is running."

@ask.launch
def startSkill():
    quote = getYodaQuote()
    return question(quote + '... Do you want more?')

@ask.intent("YesIntent")
def shareQuote():
    quote = getYodaQuote()
    return question(quote + '... Do you want more?')

@ask.intent("NoIntent")
def noIntent():
    byeText = 'Lol... OK... Bye'
    return statement(byeText)

