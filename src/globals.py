import json


def load_globals(file_path) -> dict:
    """Load experiment settings from a JSON file."""
    with open(file_path, 'r') as file:
        globals_dict = json.load(file)
        
    return globals_dict


FILE_PATH = 'experiment.json'
SETTINGS = load_globals(FILE_PATH)
