import logging as x

x.basicConfig(
    filename=".temp/cool.txt",
    filemode="a",
    level=x.NOTSET,
    format="%(asctime)s - %(levelname)s - %(levelno)s - %(message)s",
)

logger = x.getLogger()

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.fatal("This is a fatal message")
logger.critical("This is a critical message")


class Triangle:
    def __init__(self, base, height):
        logger.info("Calculating area of triangle")
        area = 0.5 * base * height
        logger.info(f"Area calculated: {area}")
        print(area)
        logger.info("Area printed successfully")


Triangle(10, 5)
