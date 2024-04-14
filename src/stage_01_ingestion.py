import os
import sys
from pathlib import Path

root = str(Path(__file__).resolve().parents[1])
sys.path.append(root)

from utils.logger import setup_logging
from utils.config import get_config
import logging
import zipfile
import pandas as pd

# setting up the logger
setup_logging()
logger = logging.getLogger(__name__)

def main():
    config = get_config()
    raw_data_path = config['paths']['raw_data']
    processed_data_path = config['paths']['processed_data']

    logger.info('Start data Ingestion...')

    # Checking if the raw data zip file exists
    if not os.path.exists(raw_data_path):
        logger.info(f'The zip file doesn\'t exist :( {raw_data_path}')
        return 
    
    # Checking if the processed data dir exists, if not let create one
    processed_dir = os.path.dirname(raw_data_path)
    if not os.path.exists(processed_dir):
        logger.info(f'Creating dir for processed data: {processed_dir}')
        os.makedirs(processed_dir)

    # Extracting dataset from zip file
    try:
        with zipfile.ZipFile(raw_data_path, 'r') as zip:
            logger.info(f'Extracting data from {raw_data_path}...')
            zip.extractall(processed_dir)
        logging.info('Data extraction complete.')

    except Exception as e:
        logger.error(f'Failed to extract data: {e}')
        return 
    
    csv_files = [f for f in os.listdir(processed_dir) if f.endswith('.csv')]
    if not csv_files:
        logger.error('No CSV files found!')
        return
    elif len(csv_files) > 1:
        logger.warning('Multiple csv files found!, using the first one listed.')

    ################# Here, you can adjust the logic to handle multiple csv files ##################

    csv_path = os.path.join(processed_dir, csv_files[0])

    # Loading the csv into a DataFrame
    try:
        df = pd.read_csv(csv_path)
        logger.info(f'Data loaded from {csv_path}')
        logger.info(df.head())
    except Exception as e:
        logger.error(f'Failed to load data: {e}')
        return
    
    logger.info('Data ingestion completed.')

if __name__ == '__main__':
    main()







