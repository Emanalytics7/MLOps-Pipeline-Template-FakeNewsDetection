from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'FAKE-NEWS-DETECTION'

files_list = [
    '.github/workflows/.gitkeep',
    'data/',
    'notebooks/',
    'models/',
    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_preprocessing.py',
    'src/components/training.py',
    'src/pipeline/__init__.py',
    'results/metrics.json',
    'logs/',
    'requirement.txt',
    'README.md',
    'setup.py',
    'Dockerfile'
    ]


for filepath in files_list:
    full_path = Path(project_name) / filepath
    if full_path.suffix:
        full_path.parent.mkdir(parents=True, exist_ok=True)
        if not full_path.exists():
            full_path.touch()   # Create file.
            logging.info(f'Created empty file: {full_path}')
        else:
            logging.info(f'File already exists: {full_path}')

    else:  # Intented to be a directory
        full_path.mkdir(parents=True, exist_ok=True)
        logging.info(f'Created directory: {full_path}')
