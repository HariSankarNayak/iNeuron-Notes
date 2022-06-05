from distutils.debug import DEBUG
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="./log_file.log",
    format="%(asctime)s %(levelname)s %(module)s => %(message)s ",
    datefmt="%d-%m-%Y %H:%M:%S",
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

