import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from src.pipelines.data_ingestion import DataIngestion
import logging
import os
import re

data = DataIngestion('./artifacts/data/datasets/processed_data', './logs')
class TextPreprocessing:
    def __init__(self, log_dir='logs'):
        self.log_dir = log_dir
        self.setup_logging()

    def setup_logging(self):

        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        logging.basicConfig(filename=os.path.join(self.log_dir, 'text_preprocessing.log'),
                            level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(message)s')
        logging.info('Text preprocessing logging setup complete.')

    def clean_text(self, text):
        """
        Cleans the text by removing non-alphanumeric characters, converting to lowercase, and removing stopwords.
        Lemmatization is also applied to each word.

        :param text: The text to clean.
        :return: Cleaned text.
        """
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        
        # Remove non-alphanumeric characters
        text = re.sub(r'\W', ' ', text)
        # Remove single characters
        text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
        # Remove single characters from the start
        text = re.sub(r'\^[a-zA-Z]\s+', ' ', text)
        # Replace multiple spaces with a single space
        text = re.sub(r'\s+', ' ', text, flags=re.I)
        # Converting to Lowercase
        text = text.lower()

        # Lemmatization and removing stopwords
        tokens = text.split()
        tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
        cleaned_text = ' '.join(tokens)

        return cleaned_text

    def vectorize_text(self, corpus):
        """
        Converts the corpus into a matrix of TF-IDF features.

        :param corpus: The corpus to vectorize.
        :return: TF-IDF matrix.
        """
        vectorizer = TfidfVectorizer(max_features=5000, min_df=5, max_df=0.7)
        X = vectorizer.fit_transform(corpus).toarray()
        logging.info('Text vectorization completed.')
        return X

    def preprocess_data(self, df, text_column='text'):
        """
        Preprocesses the DataFrame by cleaning and vectorizing the text.

        :param df: DataFrame containing the text data.
        :param text_column: The name of the column containing text.
        :return: Tuple of processed features (X) and labels (y).
        """
        # Clean the text
        df[text_column] = df[text_column].apply(self.clean_text)
        logging.info('Text cleaning completed.')

        # Vectorize the text
        X = self.vectorize_text(df[text_column])
        
        # Assuming 'label' is the column for labels
        y = df['label'].values
        return X, y