from flask import Flask
from flask_ask import Ask, statement, request
import requests

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('GetCardCountIntent')
def get_card_count():
	# Send a GET request to Flask backend to get card count and optimized bet
	response = requests.get('http://<your-flask-backend-url>/alexa_card_info', params={
		'card_sequence': 'Ace of Spades, 5 of Diamonds'
	})

	if response.status_code == 200:
		data = response.json()
		predicted_count = data['predicted_count']
		optimized_bet = data['optimized_bet']
		apl_document = data['apl_document']

		# Return the result with APL rendering directive
		return statement("Here is the card count and prediction.").add_directive({
			'type': 'Alexa.Presentation.APL.RenderDocument',
			'token': 'card-count-token',
			'document': apl_document
		})

if __name__ == '__main__':
	app.run(debug=True, port=3000)
