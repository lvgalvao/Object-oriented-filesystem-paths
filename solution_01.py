import os # various operating system interfaces
import shutil # high-level file operations
from glob import glob # unix style pathname pattern expansion
from os import path # path name manipulations

# check then delete a folder if exist
if path.exists('weak_against_electric'):
    shutil.rmtree('weak_against_electric')

# create a new folder
os.mkdir('weak_against_electric')

# types weak against electric
types = ['type_fire', 'type_flying']

# copy these files to the new folder
for type in types:
    for file in glob(f'pokemon/{type}/*.json'):
        shutil.copy(file, 'weak_against_electric')