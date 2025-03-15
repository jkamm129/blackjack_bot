import React, { useEffect, useRef } from 'react';

function LiveFeed() {
	const videoRef = useRef(null);

	useEffect(function() {
		function streamVideo() {
			const video = videoRef.current;
			// Connect to the Raspberry Pi's video feed (e.g., using an MJPEG stream)
			video.src = 'http://<raspberry-pi-ip>:8080/video';
			video.play();
		}
		streamVideo();
	}, []);

	return (
		<div>
			<h3>Live Video Feed</h3>
			<video ref={videoRef} width="640" height="480" controls />
		</div>
	);
}

export default LiveFeed;

