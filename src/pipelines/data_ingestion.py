import pandas as pd
import os
import logging

logging.basicConfig(filename='logs/data_ingestion.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class DataIngestion:
    def __init__(self, dataset_dir, log_dir='logs'):
        self.dataset_dir = dataset_dir
        self.log_dir = log_dir
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(filename=os.path.join(self.log_dir, 'data_ingestion.log'),
                            level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(message)s')
        logging.info('Logging setup complete.')

    def load_data(self, file_path, file_name):
        """
        Loads the data from the specified file path and file name.
        :param file_path: The path to the file.
        :param file_name: The name of the file.
        :return: A pandas dataframe.
        """
        file_path = os.path.join(self.dataset_dir, file_name)
        try:
            df = pd.read_csv(file_path)
            logging.info(f'Data Loaded Successfully from {file_path}')
            return df
        except Exception as e:
            logging.error(f'Error loading data from {file_path}: {e}')
            raise
