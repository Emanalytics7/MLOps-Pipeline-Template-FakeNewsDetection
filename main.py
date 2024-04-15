import argparse
import sys
from pathlib import Path

root = str(Path(__file__).resolve().parents[1])
sys.path.append(root)
from src.pipeline.stage_01_ingestion import DataIngestor
from src.pipeline.stage_02_preprocessing import TextDataProcessor
from src.pipeline.stage_03_training import TextModelTrainer
from src.pipeline.stage_04_evaluation import ModelEvaluator
from src.utils.logger import setup_logging  


setup_logging()

def main(args):
    if args.step == 'ingest':
        ingestor = DataIngestor()
        ingestor.run()
    elif args.step == 'preprocess':
        processor = TextDataProcessor('config/settings.ini')
        processor.run()
    elif args.step == 'train':
        trainer = TextModelTrainer('config/settings.ini')
        trainer.run()
    elif args.step == 'evaluate':
        evaluator = ModelEvaluator('config/settings.ini')
        evaluator.run()

    else:
        raise ValueError(f'Invalid step: {args.step}')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the MLOps pipeline steps")
    parser.add_argument('step', choices=['ingest', 'preprocess', 'train', 'evaluate'],
                        help="The pipeline step to run")
    args = parser.parse_args()

    main(args)
