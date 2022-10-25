from pathlib import Path
from shutil import rmtree

# set output path
output_path = Path('weak_against_electric')

# check then delete a folder if exist
if output_path.exists():
    rmtree(output_path)

# create a new folder
output_path.mkdir()

# types weak against electric
types = ['type_fire', 'type_flying']

# copy these files to the new folder
for type in types:
    for file in Path(f'pokemon/{type}').glob('*.json'):
        new_file = output_path / file.name
        new_file.write_text(file.read_text())