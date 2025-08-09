import os
from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # allow requests from your frontend

# MongoDB connection


client = MongoClient(os.getenv("MONGO_URI"))
db = client["Rural"]  # your DB name
courses_collection = db["Courses"]  # your collection name


@app.route("/api/courses", methods=["GET"])
def get_courses():
    courses = list(courses_collection.find({}, {"_id": 0}))

    # Add placeholder values for fields your frontend expects
    for idx, course in enumerate(courses):
        course["id"] = idx + 1
        course["description"] = "Learn more about " + course["title"]
        course["category"] = "General"
        course["level"] = "Beginner"
        course["rating"] = 4.5
        course["duration"] = "Self-paced"
        course["students"] = 0
        course["provider"] = course["platform"]
        course["price"] = "Free"

    return jsonify(courses)

if __name__ == "__main__":
    app.run(debug=False)
