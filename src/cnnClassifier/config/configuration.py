import os
from pathlib import Path
from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig




class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILEPATH,
            params_filepath = PARAMS_FILEPATH):
        
        self.config = read_yaml(config_filepath)
        self.param = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_prepare_base_model_config(self)-> PrepareBaseModelConfig:
        
