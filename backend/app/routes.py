from flask import Flask, request, jsonify
# from app.ai_predictor import

app = Flask(__name__)

@app.route('/process_cards', methods=['POST'])
def process_cards():
	# Receive JSON data from Raspberry Pi
	data = request.get_json()
	card_sequence = data.get('card_sequence', '')

	# TODO: Setup prediction modal here
	predicted_count = 100
	optimized_bet = 400

	# TODO: Construct the APL document for Echo Show display
	apl_document = {
		"type": "APL",
		"version": "1.4",
		"mainTemplate": {
			"items": [
				{
					"type": "Text",
					"text": f"Card Count: {predicted_count}",
					"fontSize": "50px",
					"color": "black",
					"align": "center"
				},
				{
					"type": "Text",
					"text": f"Optimized Bet: ${optimized_bet}",
					"fontSize": "40px",
					"color": "blue",
					"align": "center"
				}
			]
		}
	}

	# Send the APL document to the Alexa skill
	send_to_alexa(apl_document)

	return jsonify({
		'card_sequence': card_sequence,
		'predicted_count': predicted_count,
		'optimized_bet': optimized_bet,
		'apl_document': apl_document
	})

def send_to_alexa(apl_document):
	# For testing, this function would be a placeholder to simulate sending APL to Alexa
	print("Sending APL document to Alexa:", apl_document)

# Run Flask data fetching server
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5025)
