import logging

format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename="hello.log", level=logging.DEBUG, format=format,
                    datefmt="%d/%m/%y %I:%M:%S %p")
logger = logging.getLogger(__file__)

logger.info("Mensagem informativa")
logger.debug("Mensagem de debug")
logger.error("Um erro aconteceu")