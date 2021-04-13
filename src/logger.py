import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('errors.log', mode='w')
formatter = logging.Formatter('%(asctime)s: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)