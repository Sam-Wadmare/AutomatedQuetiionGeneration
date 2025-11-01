from flask import Flask, jsonify, render_template
import pandas as pd
from transformers import pipeline
import random

app = Flask(__name__)

# Load model once
generator = pipeline("text2text-generation", model="valhalla/t5-small-qg-prepend")

# Load your CSV
df = pd.read_csv('clean_general_aptitude_dataset.csv', sep=';')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate_question():
    # Pick a random question from CSV
    context = df['Question'].sample(1).iloc[0]
    
    # Generate new question using AI
    generated = generator("generate question: " + context)
    question = generated[0]['generated_text']
    
    # Keep original options (or create dummy options if you want AI to generate later)
    row = df[df['Question'] == context].iloc[0]
    options = [row['Option A'], row['Option B'], row['Option C'], row['Option D']]
    answer = row['Answer']
    
    return jsonify({
        "question": question,
        "options": options,
        "answer": answer
    })

if __name__ == '__main__':
    app.run(debug=True)
