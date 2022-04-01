import logging

logging.basicConfig(filename='q4.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

a = list(range(1,21))

try:
    squared_numbers = logging.info(list(map(lambda x:x**2, a)))
except Exception as err:
    logging.info(f"Exception: '{err}'")