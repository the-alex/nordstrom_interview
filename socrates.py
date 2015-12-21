import json
import logging
import multiprocessing
import os
import re
import requests
import sodapy
import time
import unicodedata


# Core Settings
DATA_FORMAT = 'csv'
SLEEP_TIME = 60

# General Settings and Datasets
CONFIG_LOC = './config.json'
CONFIG = {}

def load_settings():
    """
    Load settings from config.json
    """
    global CONFIG
    with open(CONFIG_LOC) as f:
        text = f.read()
    CONFIG = json.loads(text)


def create_valid_file_name(ds):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens. Adapted from Django "slugify" method.
    """
    file_name = ds['name']
    file_name = unicodedata.normalize('NFKD', file_name).encode('ascii', 'ignore')
    file_name = unicode(re.sub('[^\w\s-]', '', file_name).strip().lower())
    file_name = re.sub('[-\s]+', '-', file_name)

    file_name = file_name + '.' + CONFIG['ds_format']
    return file_name


def update_dataset(ds):
    """
    Takes a dataset as desribed by a dictionary and pulls the latest
    version of that dataset from Socrata.
    """

    # Create the data directory if it doesn't already exist
    if not os.path.exists(CONFIG['data_path']):
        os.makedirs(CONFIG['data_path'])

    # Get the url endpoint for this dataset
    target = '%s.%s' % (ds['endpoint'], CONFIG['ds_format'])
    target = target + '?$limit=50000'
    req = requests.get(target)

    # Generate valid file path
    write_path = CONFIG['data_path'] + create_valid_file_name(ds)

    # If API call successful
    if req.status_code == 200:
        confirm = 'Writting from {0} to {1}'.format(target, write_path)
        logging.info(confirm)
        
        with open(write_path, 'w') as f:
            f.write(req.text.encode('utf8'))

    else:
        logging.info('Call to "update_dataset" for "%s" failed' % ds['name'])



def main():
    # Load settings from config.json file.
    load_settings()

    # Initialize logging
    if not os.path.exists(CONFIG['logs_path']):
        os.makedirs(CONFIG['logs_path'])

    logging.basicConfig(filename='logs/socrates.log',
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.DEBUG)

    # Event Loop
    while True:
        # Update Datasets
        datasets = CONFIG['datasets']

        # Number of workers should not exceed 4
        num_workers = len(datasets) if len(datasets) < 4 else 4
        pool = multiprocessing.Pool(num_workers)
        
        # Assign workers to update_dataset function
        pool.map(update_dataset, datasets)

        logging.info('DONE :: Going to sleep now for %s seconds' % str(SLEEP_TIME))
        time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    main()
