from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector
app = Flask("emotion detector")

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotionDetector():
    query = request.args.get("textToAnalyze")
    result = emotion_detector(query)
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

