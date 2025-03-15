blackjack_bot/
├── frontend/                     # React frontend (used for data analytics)
│   ├── public/
│   │   └── index.html            # Basic HTML for frontend
│   ├── src/
│   │   ├── components/           # React components (optional)
│   │   ├── App.js                # Main React component
│   │   ├── App.css               # Global styles
│   ├── package.json              # React dependencies and scripts
│   └── .gitignore                # Ignore unnecessary frontend files
├── backend/                      # Flask API (AI + Backend)
│   ├── app/
│   │   ├── __init__.py           # Initialize Flask app
│   │   ├── routes.py             # Routes for receiving requests from Raspberry Pi & Alexa
│   │   ├── ai_predictor.py       # AI model for card prediction and bet optimization
│   ├── run.py                    # Entry point for running the Flask app
│   └── .gitignore                # Ignore unnecessary backend files
├── embedded/                     # Raspberry Pi (Card Recognition + Display)
│   ├── raspberrypi/              # Raspberry Pi-specific code
│   │   ├── card_recognition.py   # Card recognition with OpenCV
│   │   ├── camera_setup.py       # Setting up camera for card detection
├── alexa-skill/                  # Alexa skill to communicate with backend
│   ├── alexa_skill.py            # Python code for the Alexa skill
│   └── .gitignore                # Ignore unnecessary files for Alexa skill
└── README.md                     # Project documentation (overview, setup instructions)