import logging
from .config import LOG_NAME, LOG_LEVEL, LOG_FILE, LOG_FORMAT, ENCODING

class Logger:
    @staticmethod
    def setup_logger(name=LOG_NAME, log_file=LOG_FILE, level=LOG_LEVEL):
        logger = logging.getLogger(name)
        
        if not logger.handlers:
            logger.setLevel(level)
            formatter = logging.Formatter(LOG_FORMAT)

            file_handler = logging.FileHandler(log_file, encoding=ENCODING)
            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
