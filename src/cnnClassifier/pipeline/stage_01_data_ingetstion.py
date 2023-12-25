from cnnClassifier.config import ConfigurationManager
from cnnClassifier.components import DataIngestion
from cnnClassifier import logger
from collections import namedtuple
from pathlib import Path
import os
# os.chdir('/Users/praveenhome/Desktop/PRAVEENBASE/AWSDEVOPS/AWSDEVOPS2023/cnnClassifier/src/')
# sys.path.append("Users/praveenhome/Desktop/PRAVEENBASE/AWSDEVOPS/AWSDEVOPS2023/cnnClassifier/src/")
# CONFIG_FILE_PATH = Path("/config/config.yaml")



class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(sef):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_and_clean()