from pathlib3x import Path # oo filesystem paths and hl file operations

# set output path
output_path = Path('weak_against_electric')

# delete a folder if exist
output_path.rmtree(ignore_errors=True)

# create a new folder
output_path.mkdir()

# types weak against electric
types = ['type_fire', 'type_flying']

# copy these files to the new folder
for type in types:
    for file in Path(f'pokemon/{type}').glob('*.json'):
        new_file = output_path / file.name
        file.copy(new_file)