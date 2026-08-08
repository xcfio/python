import logging as x
import json
import os

os.makedirs(".temp", exist_ok=True)


class PinoFormatter(x.Formatter):
    LEVEL_MAP = {
        x.DEBUG: 20,
        x.INFO: 30,
        x.WARNING: 40,
        x.ERROR: 50,
        x.CRITICAL: 60,
    }

    def format(self, record):
        log = {
            "level": self.LEVEL_MAP.get(record.levelno, record.levelno),
            "time": int(record.created * 1000),
            "msg": record.getMessage(),
        }
        return json.dumps(log)


handler = x.FileHandler(".temp/cool.txt", mode="a")
handler.setFormatter(PinoFormatter())

logger = x.getLogger()
logger.setLevel(x.NOTSET)
logger.addHandler(handler)


class Triangle:
    def __init__(self, base, height):
        logger.info("Calculating area of triangle")
        area = 0.5 * base * height
        logger.info(f"Area calculated: {area}")
        print(area)
        logger.info("Area printed successfully")


Triangle(10, 5)
