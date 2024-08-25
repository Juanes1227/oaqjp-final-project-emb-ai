"""
server.py

This module contains a Flask web application with two routes:
1. /emotionDetector - Analyzes the provided text to detect emotions and returns the result.
2. / - Renders the index HTML page.

Dependencies:
- Flask
- EmotionDetection.emotion_detection
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the provided text to detect emotions and returns the result.
    Retrieves the text from the request, passes it to the emotion detector,
    and formats the response to display the emotion scores and the dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Check if the label is None, indicating an error or invalid input
    if response['dominant_emotion'] is None:
        result = "Invalid text! Try again."
    else:
        # Determine the dominant emotion
        dominant_emotion = response['dominant_emotion']

        # Remove the dominant emotion from the scores
        emociones_sin_dominante = {
            k: response[k] for k in response if k != 'dominant_emotion'
        }

        # Create the string representation of the emotion scores
        emociones_texto = ', '.join(
            f"'{key}': {value}" for key, value in emociones_sin_dominante.items()
        )

        # Add the dominant emotion to the result
        result = (
            f"For the given statement, the system response is {emociones_texto}. "
            f"The dominant emotion is {dominant_emotion}."
        )
    
    # Return the result
    return result

@app.route("/")
def render_index_page():
    """
    Renders the index HTML page.
    Returns the 'index.html' template.
    """
    return render_template('index.html')

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
