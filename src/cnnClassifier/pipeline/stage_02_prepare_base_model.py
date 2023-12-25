from cnnClassifier.config import ConfigurationManager
from cnnClassifier.components import PrepareBaseModel
from cnnClassifier import logger
from collections import namedtuple
from pathlib import Path
import os
# os.chdir('/Users/praveenhome/Desktop/PRAVEENBASE/AWSDEVOPS/AWSDEVOPS2023/cnnClassifier/src/')
# sys.path.append("Users/praveenhome/Desktop/PRAVEENBASE/AWSDEVOPS/AWSDEVOPS2023/cnnClassifier/src/")
# CONFIG_FILE_PATH = Path("/config/config.yaml")



class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    def main(sef):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()