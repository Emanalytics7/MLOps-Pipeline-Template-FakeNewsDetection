import logging
import os
import zipfile
import csv
from dataclasses import dataclass
from src.utils.logger import setup_logger

logger = setup_logger()

@dataclass
class DataIngestionConfig:
    zip_file_path: str
    log_file_path: str
    output_dir: str

class DataIngestion:
    def __init__(self, config):
        self.config = config
        self.logger = logger
    
    def extract_zip_file(self):
        try:
            with zipfile.ZipFile(self.config.zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(self.config.output_dir)
            self.logger.info("Zip file extracted successfully!")
        except Exception as e:
            self.logger.error(f"Error in extracting zip file: {e}")

config = DataIngestionConfig(zip_file_path='data/processed_data.zip', log_file_path='logs', output_dir='data/')
data_ingestion = DataIngestion(config)
data_ingestion.extract_zip_file()