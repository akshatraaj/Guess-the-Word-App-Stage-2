from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
      "inputs": 6,
      "category": "What is the SI unit of Force?",
      "word": "Newton"
    },
    {
      "inputs": 4,
      "category": "How many rings of OLYMPIC?",
      "word": "five"
    }
]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run()
