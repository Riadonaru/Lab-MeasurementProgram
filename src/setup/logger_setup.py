import os
import logging

def set_logger() -> None:
    """Set up the logger for the application."""
    log_file = os.path.join(os.getcwd(), "logs\\app.log")

    logging.basicConfig(
        level=logging.INFO,                 # Minimum level to log
        format="[%(asctime)s] - %(levelname)s : %(message)s",
        handlers=[
            logging.FileHandler(log_file), # Log to file
        ]
    )
    logging.info("Logger initialized.")
    return