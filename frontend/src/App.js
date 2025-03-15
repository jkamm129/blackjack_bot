import './App.css';
import LiveFeed from './components/livefeed';
import CardSequence from './components/card_sequence';
import Prediction from './components/prediction';
import React, { useState, useEffect } from 'react';

function App() {
	const [cardSequence, setCardSequence] = useState('');
	const [predictedCount, setPredictedCount] = useState(null);
	const [optimizedBet, setOptimizedBet] = useState(null);
	return (
		<div className="App">
			<header className="App-header">
				<p>
					This will be the data analytics site
				</p>
			</header>
		</div>
	);
}

export default App;
