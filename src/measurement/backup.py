import os
import time
import pickle
import logging

from config import BACKUP_PATH


def ensure_backup_directory() -> None:
    """Ensures the backup directory exists and creates it if it doesn't."""
    path = os.path.join(os.getcwd(), BACKUP_PATH)
    os.makedirs(path, exist_ok=True)
    logging.debug(f"Backup directory ensured at: {path}")

def generate_backup_filename() -> str:
    """Generate a timestamped backup filename in the backup directory."""
    timestamp = time.strftime("%d-%m-%Y_%H-%M-%S")
    filename = f"backup_{timestamp}.pkl"
    return os.path.join(os.getcwd(), BACKUP_PATH, filename)

def save_backup(data: object) -> None:
    """Saves the given data object to a backup file."""
    ensure_backup_directory()
    backup_file = generate_backup_filename()
    with open(backup_file, 'wb') as f:
        pickle.dump(data, f)
    logging.info(f"Backup saved to: {backup_file}")
        
def load_backup(backup_file: str) -> object:
    """Loads and returns the data object from the specified backup file."""
    try:
        with open(backup_file, 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError as e:
        backup_file = os.path.join(os.getcwd(), BACKUP_PATH, backup_file)
        with open(backup_file, 'rb') as f:
            data = pickle.load(f)
    logging.info(f"Backup loaded from: {backup_file}")
    return data