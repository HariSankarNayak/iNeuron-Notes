import logging

class scrapLogger:

    def ineuron_scrap_logger(file_name='log_file.log', log_level=logging.DEBUG):
        logger = logging.getLogger("demo")
        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler("log_file.log")
        formater = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        console_handler.setFormatter(formater)
        file_handler.setFormatter(formater)
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        return logger