"""
Server.py
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("emotion detector")
@app.route('/')
def index():
    """Function index."""
    return render_template('index.html')
@app.route("/emotionDetector")
def emotions_detector():
    """Function emotions_detector."""
    query = request.args.get("textToAnalyze")
    if not query or query.strip() == "":
        return {'anger': None,
        'disgust': None, 
        'fear': None, 
        'joy': None, 
        'sadness': None, 
        'dominant': None},400
    result = emotion_detector(query)
    if result.get("dominant_emotion") is None:
        return {"error_message": "Invalid text! Please try again!"}, 400
    return (result), 200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
