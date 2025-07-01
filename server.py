"""
server.py

This module initializes and runs the Flask web server for the application.

It defines application routes, handles incoming HTTP requests, and returns
appropriate responses. The server runs in development mode and listens on
the default Flask port (5000) unless otherwise specified.

Author: Om Prakash Patel
Date: 01-07-2025
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emt_detector():
    """
    The purpose of this function is two fold. 
    First, the function should send a GET request to the HTML interface to receive the input text.
    Second function, call your sentiment_analyzer application with text_to_analyze as the argument.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the emotions from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if anger is None:
        return "Invalid text! Please try again!"

    return (
    f"For the given statement, the system response is 'anger': {anger}, "
    f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
    f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    This function should simply run the render_template function on the HTML template
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
