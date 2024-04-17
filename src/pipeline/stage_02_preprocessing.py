import sys
import re
import logging
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from pathlib import Path

root = str(Path(__file__).resolve().parents[1])
sys.path.append(root)

from utils.config import get_config
from utils.logger import setup_logging
import nltk

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

class TextDataProcessor:
    def __init__(self, config_path):
        setup_logging()
        self.logger = logging.getLogger(__name__)
        self.config = get_config(config_path)
        self.raw_data_path = self.config['paths']['data']
        self.feature_path = self.raw_data_path.replace('raw_data.csv', 'features.pkl')
        self.label_path = self.raw_data_path.replace('raw_data.csv', 'labels.pkl')
        self.vectorizer_path = self.config['path']['vectorizer']

    def load_data(self):
        """ Load the dataset from a CSV file. """
        try:
            df = pd.read_csv(self.raw_data_path)
            self.logger.info("Data loaded successfully.")
            return df
        except Exception as e:
            self.logger.error(f"Failed to load data: {e}")
            return None

    def clean_text(self, text):
        """ Clean text by removing unwanted characters and stopwords. """
        text = text.lower()
        text = re.sub(r'<.*?>', '', text)
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        text = re.sub(r'[^a-z\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        return ' '.join([lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words])

    def preprocess_data(self, data):
        """ Preprocess the data: clean and vectorize text. """
        data['text'] = data['text'].apply(self.clean_text)
        self.vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'), max_features=5000)
        features = self.vectorizer.fit_transform(data['text']).toarray()
        self.logger.info("Data preprocessing complete.")
        return features, data['label'].values

    def save_data(self, features, labels):
        """ Save features and labels to files. """
        with open(self.feature_path, 'wb') as f_feature:
            pickle.dump(features, f_feature)
        with open(self.label_path, 'wb') as f_label:
            pickle.dump(labels, f_label)
        with open(self.vectorizer_path, 'wb') as f_vectorizer:
            pickle.dump(self.vectorizer, f_vectorizer)
        self.logger.info(f"Features and labels saved to {self.feature_path} and {self.label_path} respectively.")

    def run(self):
        """ Run the data processing pipeline. """
        data = self.load_data()
        if data is not None:
            features, labels = self.preprocess_data(data)
            self.save_data(features, labels)

