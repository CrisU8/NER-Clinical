import os
from pathlib import Path
import logging  

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

proyect_name = 'clinical-NER'

list_of_files = [
    'github/workflows/.gitkeep',
    f'src/{proyect_name}/__init__.py',
    f'src/{proyect_name}/components/__init__.py',
    f'src/{proyect_name}/utils/__init__.py',
    f'src/{proyect_name}/config/__init__.py',
    f'src/{proyect_name}/config/configuration.py',
    f'src/{proyect_name}/pipeline/__init__.py',
    f'src/{proyect_name}/entities/__init__.py',
    f'src/{proyect_name}/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb'

    ]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !='':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory {filedir} for file {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Creating empty file {filepath}')
    
    else:
        logging.warning(f'File {filepath} already exists and is not empty')

