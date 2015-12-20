import sodapy
import time
import logging


DATASETS = []


if __name__ == '__main__':
    # Initialize logging
    logging.basicConfig(filename='logs/socrates.log',level=logging.INFO)

    # Check availible databases
    while True:
        # Check for new datasets.
