from app import app

# Run Flask data fetching server
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=4000)
