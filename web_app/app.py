from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import the CORS extension
import mysql.connector
import requests
from textblob import TextBlob

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the Flask app

# MySQL database initialization
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="chatbot"
)
mycursor = mydb.cursor()

# Create table if not exists
mycursor.execute('''CREATE TABLE IF NOT EXISTS chat_logs
                    (id INT AUTO_INCREMENT PRIMARY KEY,
                     request TEXT,
                     response TEXT,
                     sentiment FLOAT)''')

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    data = request.json
    msg = data.get("message", "")
    # Get response using requests module
    r = requests.post(
        "http://localhost:5002/webhooks/rest/webhook", json={"message": msg}
    )
    print("Genius says, ", end=" ")
    response = ""
    sentiment_scores = []
    for i in r.json():
        response += i["text"]
        sentiment = analyze_sentiment(i["text"])
        sentiment_scores.append(sentiment)
    # Store request, response, and sentiment score in the database
    sql = "INSERT INTO chat_logs (request, response, sentiment) VALUES (%s, %s, %s)"
    val = (msg, response, sum(sentiment_scores)/len(sentiment_scores))
    mycursor.execute(sql, val)
    mydb.commit()
    return jsonify({"response": response, "sentiment": sentiment_scores})

if __name__ == "__main__":
    app.run(debug=True)


