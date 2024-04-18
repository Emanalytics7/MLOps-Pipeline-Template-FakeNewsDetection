from flask import Flask, request, jsonify
import pickle
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re


app = Flask(__name__)

# Loading the model and vectorizer
with open('api/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('api/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# to clean the incoming data
def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    return ' '.join([lemmatizer.lemmatize(word)
                      for word in text.split()
                        if word not in stop_words])

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = data['text']
    cleaned_text = clean_text(text)
    features = vectorizer.transform([cleaned_text]).toarray()
    prediction = model.predict(features)
    
    probability = model.predict_proba(features)
    if prediction[0] == 0:
        return jsonify({'prediction':'Fake News', 
                        'probability': probability[0].tolist()})
    else:
        return jsonify({'prediction': 'Authentic News',
                         'probability': probability[0].tolist()})
if __name__ == '__main__':
    app.run(debug=True)
