import pickle
import logging
import pandas as pd
import sys
from sklearn.metrics import classification_report
from pathlib import Path

root = str(Path(__file__).resolve().parents[1])
sys.path.append(root)
from utils.config import get_config
from utils.logger import setup_logging

class ModelEvaluator:
    def __init__(self, config_path):
        setup_logging()
        self.logger = logging.getLogger(__name__)
        self.config = get_config(config_path)
        self.test_data_path = self.config['paths']['test_data']  
        self.model_path = self.config['paths']['model']

    def load_model_and_data(self):
        """ Load the model and test data from files. """
        try:
            with open(self.model_path, 'rb') as f:
                model = pickle.load(f)
            # Loading the test data 
            test_data = pd.read_csv(self.test_data_path)
            X_test = test_data.iloc[:, :-1]  
            y_test = test_data.iloc[:, -1]

            self.logger.info("Model and test data loaded successfully.")
            return model, X_test, y_test
        except Exception as e:
            self.logger.error(f"Failed to load model or test data: {e}")
            return None, None, None

    def evaluate_model(self, model, X_test, y_test):
        """ Evaluate the model using the test set and print a classification report. """
        predictions = model.predict(X_test)
        report = classification_report(y_test, predictions, zero_division=0)
        self.logger.info("Model evaluation report:\n" + report)

    def run(self):
        """ Run the model evaluation pipeline. """
        model, X_test, y_test = self.load_model_and_data()
        if model and X_test is not None:
            self.evaluate_model(model, X_test, y_test)
