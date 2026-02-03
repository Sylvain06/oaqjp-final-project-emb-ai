from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector
app = Flask("emotion detector")

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotionDetector():
    query = request.args.get("textToAnalyze")
    
    result = emotion_detection.emotion_detector(text_to_analyze)
    return {"responseText": result}


app.run(host="0.0.0.0", port=5000)