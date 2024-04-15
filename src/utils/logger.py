import logging.config
import configparser
import os

def setup_logging(default_path='config/settings.ini'):
    """Setup logging configuration"""
    config = configparser.ConfigParser()
    config.read(default_path)
    log_file_path = config['logging']['log_file']

    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(levelname)s - %(name)s: %(message)s'
            },
        },
        'handlers': {
            'default': {
                'level': 'INFO',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
            },
            'file': {
                'level': 'INFO',
                'formatter': 'standard',
                'class': 'logging.FileHandler',
                'filename': log_file_path,
                'mode': 'a',
            },
        },
        'loggers': {
            '': {  # root logger
                'handlers': ['default', 'file'],
                'level': 'INFO',
                'propagate': True
            },
        }
    })

    # ensure log dir exists
    if not os.path.exists(os.path.dirname(log_file_path)):
        os.makedirs(os.path.dirname(log_file_path))

    # Just to confirm logging is set up
    logger = logging.getLogger(__name__)
    logger.info('Logging is set up.')
