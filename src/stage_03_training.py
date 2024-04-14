import pickle
import logging
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from utils.config import get_config
from utils.logger import setup_logging

class TextModelTrainer:
    def __init__(self, config_path):
        setup_logging()
        self.logger = logging.getLogger(__name__)
        self.config = get_config(config_path)
        self.feature_path = self.config['paths']['features']
        self.label_path = self.config['paths']['labels']
        self.model_path = self.config['paths']['model']

    def load_data(self):
        """ Load features and labels from pickle files. """
        try:
            with open(self.feature_path, 'rb') as f:
                features = pickle.load(f)
            with open(self.label_path, 'rb') as f:
                labels = pickle.load(f)
            self.logger.info("Features and labels loaded successfully.")
            return features, labels
        except Exception as e:
            self.logger.error(f"Failed to load features/labels: {e}")
            return None, None

    def train_model(self, features, labels):
        """ Train a logistic regression model using the provided features and labels. """
        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        self.logger.info("Model training completed.")
        return model

    def save_model(self, model):
        """ Save the trained model to a file. """
        with open(self.model_path, 'wb') as f:
            pickle.dump(model, f)
        self.logger.info(f"Model saved to {self.model_path}")

    def run(self):
        """ Run the model training pipeline and save the model. """
        features, labels = self.load_data()
        if features is not None and labels is not None:
            model = self.train_model(features, labels)
            self.save_model(model)

if __name__ == '__main__':
    trainer = TextModelTrainer('config/settings.ini')
    trainer.run()
