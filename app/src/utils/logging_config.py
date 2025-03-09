import logging

def setup_logging():
    """
    Sets up the logging configuration for the entire project.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
        handlers=[
            logging.StreamHandler(), 
        ]
    )