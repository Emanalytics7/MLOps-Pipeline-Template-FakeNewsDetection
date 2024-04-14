import os
import sys
import logging
import zipfile
import pandas as pd
from pathlib import Path

root = str(Path(__file__).resolve().parents[1])
sys.path.append(root)

from utils.logger import setup_logging
from utils.config import get_config

class DataIngestor:
    def __init__(self):
        setup_logging()
        self.logger = logging.getLogger(__name__)
        self.config = get_config()
        self.raw_data_path = self.config['paths']['raw_data']
        self.processed_data_path = self.config['paths']['processed_data']

    def check_directory(self, path):
        """ Check if directory exists and create it if it does not. """
        if not os.path.exists(path):
            self.logger.info(f'Creating directory: {path}')
            os.makedirs(path)

    def extract_data(self):
        """ Extract data from a zip file into the processed directory. """
        try:
            with zipfile.ZipFile(self.raw_data_path, 'r') as zip_ref:
                self.logger.info(f'Extracting data from {self.raw_data_path}...')
                zip_ref.extractall(self.processed_data_path)
            self.logger.info('Data extraction complete.')
        except Exception as e:
            self.logger.error(f'Failed to extract data: {e}')
            return False
        return True

    def find_csv_files(self):
        """ Find all CSV files in the processed directory. """
        csv_files = [f for f in os.listdir(self.processed_data_path) if f.endswith('.csv')]
        if not csv_files:
            self.logger.error('No CSV files found!')
            return None
        elif len(csv_files) > 1:
            self.logger.warning('Multiple CSV files found; using the first one listed.')
        return csv_files[0]

    def load_data(self, file_name):
        """ Load data from a CSV file into a DataFrame. """
        csv_path = os.path.join(self.processed_data_path, file_name)
        try:
            df = pd.read_csv(csv_path)
            self.logger.info(f'Data loaded successfully from {csv_path}')
            return df
        except Exception as e:
            self.logger.error(f'Failed to load data: {e}')
            return None

    def run(self):
        self.logger.info('Starting data ingestion...')
        if not os.path.exists(self.raw_data_path):
            self.logger.info(f'The zip file doesn\'t exist: {self.raw_data_path}')
            return
        self.check_directory(self.processed_data_path)
        if self.extract_data():
            csv_file = self.find_csv_files()
            if csv_file:
                df = self.load_data(csv_file)
                if df is not None:
                    self.logger.info(df.head())
                    self.logger.info('Data ingestion completed.')

if __name__ == '__main__':
    ingestor = DataIngestor()
    ingestor.run()
