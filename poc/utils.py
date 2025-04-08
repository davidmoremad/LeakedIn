# Create some utility functions for the project:
# Logging class with colors
# Requests methods to get data from an API
# Read and write CSV files
# Read and write YAML files


import os
import json
import logging
import requests
import csv
import yaml
from datetime import datetime

# Logging class with colors and formatting
# -----------------------------------------------------
class Logger(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[94m',  # Blue
        'INFO': '\033[92m',   # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',  # Red
        'CRITICAL': '\033[95m',  # Magenta
        'RESET': '\033[0m'    # Reset to default
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        message = super().format(record)
        return f"{log_color}{message}{self.COLORS['RESET']}"
    
def setup_logger(name, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create formatter
    formatter = Logger('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(ch)
    
    return logger

# Initialize logger
logger = setup_logger(__name__)

# Read and write files
# -----------------------------------------------------

def read_csv(file_path):
    """
    Read a CSV file and return its content as a list of dictionaries.
    """
    if not os.path.exists(file_path):
        logger.error(f"File {file_path} does not exist.")
        return []

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    
    logger.info(f"Read {len(data)} rows from {file_path}.")
    return data

def write_csv(file_path, data):
    """
    Write a list of dictionaries to a CSV file.
    """
    if not data:
        logger.warning("No data to write.")
        return

    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    
    logger.info(f"Wrote {len(data)} rows to {file_path}.")

def read_yaml(file_path):
    """
    Read a YAML file and return its content as a dictionary.
    """
    if not os.path.exists(file_path):
        logger.error(f"File {file_path} does not exist.")
        return {}

    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    
    logger.info(f"Read YAML file: {file_path}.")
    return data


# Basic Requests methods
# -----------------------------------------------------

def get_request(url, params=None, headers=None):
    """
    Make a GET request to the specified URL with optional parameters and headers.
    """
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        logger.info(f"GET request to {url} successful.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"GET request to {url} failed: {e}")
        return None
    