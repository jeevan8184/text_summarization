import os
from pathlib import Path
import yaml
from textSummarizer.logging import logger
from box.exceptions import BoxValueError
from box import ConfigBox
from typing import Any
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"read_yamll successfully loaded for file : {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("read_yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_dirs(path_to_dirs:list,verbose=True):
        
        for dir_path in path_to_dirs:
            os.makedirs(dir_path,exist_ok=True)
            if verbose:
                logger.info(f"Created directory: {dir_path}")


@ensure_annotations
def get_size(path:Path)->str:
     
     size = round(os.path.getsize(path)/1024)
     return f"~ {size} KB"

