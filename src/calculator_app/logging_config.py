import logging

def setup_logging():
    
    logger = logging.getLogger("ScientificCalculatorApp")
    logger.setLevel(logging.INFO)

 
    if logger.hasHandlers():
        return logger

    # Configure the format for the log messages
    log_format = '%(asctime)s [%(levelname)s] - %(message)s'
    formatter = logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S')
    formatter.default_msec_format = '%s.%03d'

    # Create and configure 
    file_handler = logging.FileHandler('app.log')
    file_handler.setFormatter(formatter)


    logger.addHandler(file_handler)

    return logger