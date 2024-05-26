import os
from box.exceptions import BoxValueError
import yaml
from cnnclassifier import logger
import json
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml:Path)-> ConfigBox:
    ''' reads yaml file and returns 
    Args :
    path_to_yaml (str): path like input 
    Raises:
    ValueError:if yaml file is empty 
    e:empty file
    Returns:
    ConfigBox:ConfigBox type'''
    try:
        with open(path_to_yaml) as yaml_file:
            content =yaml.safe_load(yaml_file)
            logger.info(f"yaml file :{path_to_yaml} loaded sucessfully") 
        return ConfigBox  (content)
    except BoxValueError:
     raise ValueError("yaml file is empty ")
    except Exception as e:
        raise    
    
@ensure_annotations

def create_diretories(path_to_directories:list,verbose =True):
    '''create list if directories 
    Args:
    path_to_diectories(list):list of directories 
    ignore_log(bool,optional):ignore if multiplel dirs is to be Created '''
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at:{path}")
            
@ensure_annotations
def save_json (path:Path,data:dict):
    '''save json data
    Args :
    path (path):path to json file 
    data(dict):data to be saved in json file '''
    
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at:{path}")
    
@ensure_annotations

def load_json(path:Path)->ConfigBox:
    '''load json files data
    Args:path (path):path to json file
    Return:
    ConfigBox:data as class attributes instead of dict
    
    '''   
    with open (path) as f:
        Content =json.load(f)
    logger.info(f"json file loaded sucessfullly from :{path}")
    return ConfigBox(Content)
@ensure_annotations
def save_bin(data:Any, path:Path):
    '''save binary file
    Args:
    data(Any):data to be saved as binary 
    path(Path):path to directory '''
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at:{path}")
    
@ensure_annotations
def load_bin(path:Path)-> Any:
    '''load binary data 
    Args:
    path(path):path to the binary file
    Return:
    Any:object stored in the file'''
    data =joblib.load(path)
    logger.info(f"binary file loaded from :{path}")
    return data
@ensure_annotations
def get_size (path:Path)->str:
    '''get size in KB
    Args:
    path (path):path of the file 
    returns:
    str:size in KB
    '''
def  decodeImage(imgString, fileName):
    imgdata=base64.b64decode(imgString)
    with open(fileName,'wb') as f:
        f.Write(imgdata)
        f.close()
def encodeImageIntoBase64(croppedImagepath):
    with open (croppedImagepath,'rb') as f:
        return base64.b64decode(f.read())