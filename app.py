import sys,os
from wasteDetection.logger import logging
from wasteDetection.exception import AppException
from wasteDetection.pipeline.training_pipeline import TrainPipeline


try:
    logging.info("Data ingestion ")
    train_pipeline = TrainPipeline()
    train_pipeline.start_data_ingestion()

except Exception as e:
    raise AppException