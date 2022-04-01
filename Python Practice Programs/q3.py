from email import message
import logging

logging.basicConfig(filename='q3.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

a = [12,24,35,24,88,120,155,88,120,155]

try:
    new_list = logging.info(set(a))
except Exception as err:
    logging.info(f"Exception: '{err}'")
