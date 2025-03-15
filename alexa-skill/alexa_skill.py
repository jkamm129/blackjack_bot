from flask import Flask
from flask_ask import Ask, statement
import requests

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('GetCardCountIntent')
def get_card_count():
	# Send a GET request to Flask backend to get card count and optimized bet
	response = requests.get('https://loose-pandas-sneeze.loca.lt/alexa_card_info',
		params={
			'card_sequence': 'Ace of Spades, 5 of Diamonds'
		})

	if (response.status_code == 200):
		data = response.json()
		apl_document = data['apl_document']

		# Return the result with APL rendering directive
		return statement("Here is the card count and prediction.").add_directive({
			'type': 'Alexa.Presentation.APL.RenderDocument',
			'token': 'card-count-token',
			'document': apl_document
		})
	else:
		 return statement("There was an error retrieving the data.")

if (__name__ == '__main__'):
	app.run(debug=True, port=5024)
