from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URI)
db = client["wikiboxd"]

@app.route("/")
def home():
    try:
        db.command("ping")
        return "WikiBoxd is running and MongoDB is connected."
    except Exception as e:
        return f"WikiBoxd is running, but MongoDB connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0")