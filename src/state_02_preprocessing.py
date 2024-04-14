import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import re
from utils.config import get_config
from utils.logger import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

def load_data(file_path):
    """ Load the dataset from a CSV file. """
    try:
        df = pd.read_csv(file_path)
        logger.info("Data loaded successfully.")
        return df
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
        return None

# def clean_text(text):
#     """ Clean the text data. """
#     text = re.sub(r'\W', ' ', str(text))
#     text = text.lower()
#     text = re.sub(r'\s+[a-z]\s+', ' ', text)
#     text = re.sub(r'^[a-z]\s+', ' ', text)
#     text = re.sub(r'\s+', ' ', text)
#     return text

########### You can utilize this function, I wont because I've already cleaned the data ################


def preprocess_data(data):
    """ Preprocess the data: clean and vectorize text. """
    # data['text'] = data['text'].apply(clean_text)
    vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'), max_features=5000)
    features = vectorizer.fit_transform(data['text']).toarray()
    logger.info("Data preprocessing complete.")
    return features, data['label'].values

def main():
    config = get_config('config/settings.ini')
    raw_data_path = config['paths']['processed_data']  # Adjust if your path setting differs

    data = load_data(raw_data_path)
    if data is not None:
        features, labels = preprocess_data(data)
        # Here you can save the features and labels to files or pass them directly to the next stage

if __name__ == '__main__':
    main()
