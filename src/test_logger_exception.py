import sys
from src.exception import CustomException
from src.logger import logging

try:
    x = 10 / 0
except Exception as e:
    logging.error("Divsion By Zero Not Allowed")
    raise CustomException(e, sys)