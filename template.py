import os
from pathlib import Path
import logging

#creating log history
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# creating project structure
projeect_name = "textsummarizer"

list_of_files = [
    ".github.com/workflows/.gitkeep",
    f"src/{projeect_name}/__init__.py",
    f"src/{projeect_name}/components/__init__.py",
    f"src/{projeect_name}/utils/__init__.py",
    f"src/{projeect_name}/utils/common.py",
    f"src/{projeect_name}/logging/__init__.py",
    f"src/{projeect_name}/config/__init__.py",
    f"src/{projeect_name}/config/configuration.py",
    f"src/{projeect_name}/pipeline/__init__.py",
    f"src/{projeect_name}/entity/__init__.py",
    f"src/{projeect_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file:{filepath}")
            
    else:
        logging.info(f"{filename} already exists")