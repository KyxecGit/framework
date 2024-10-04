import logging

class Logger:
    @staticmethod
    def setup_logger(name='framework_logger', log_file='framework.log', level=logging.DEBUG):
        logger = logging.getLogger(name)
        
        if not logger.handlers:
            logger.setLevel(level)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
