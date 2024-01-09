import os
from pathlib import Path
from logger import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: %(lineno)s')

project_name = "tpod"

list_of_files=[
    ".github/workflows/.gitkeep", 
    "src/utils.py",   
    "src/components/__init__.py",
    "src/components/register.py",
    "src/components/portal_a_rid.py",
    "src/components/portal_b.py",
    "src/components/portal_c.py",
    "player_profiles/"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already existing")