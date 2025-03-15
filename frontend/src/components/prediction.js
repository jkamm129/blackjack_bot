import React from 'react';

function Prediction({ predictedCount, optimizedBet }) {
	return (
		<div>
			<h3>Predicted Count: {predictedCount}</h3>
			<h3>Optimized Bet: ${optimizedBet}</h3>
		</div>
	);
}

export default Prediction;
