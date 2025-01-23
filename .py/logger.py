import logging
import functools
import traceback

def get_logger(name="app", log_file="app.log", level=logging.DEBUG):
    """Returns a logger configured with the specified settings."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # File handler
    file_handler = logging.FileHandler(log_file, mode='a')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    file_handler.setFormatter(formatter)
    
    handler_exists = any(isinstance(handler, logging.FileHandler) for handler in logger.handlers)
    if not handler_exists:
        logger.addHandler(file_handler)
    
    return logger

# Decorator for auto-logging function execution
def log_function(logger):
    """A decorator to automatically log function execution details."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"Starting '{func.__name__}' with arguments: args={args}, kwargs={kwargs}")
            try:
                result = func(*args, **kwargs)
                logger.info(f"'{func.__name__}' completed successfully.")
                return result
            except Exception as e:
                logger.error(f"Error in '{func.__name__}': {str(e)}")
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug("Traceback:\n" + traceback.format_exc())
                raise
        return wrapper
    return decorator




































#https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/tree/master