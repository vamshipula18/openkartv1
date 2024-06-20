import inspect
import os
import logging
class Loggen:
    @staticmethod
    def loggen():
        loggerName = inspect.stack()[1][3]
        log_dir = r"C:\Users\vamsh\PycharmProjects\openKartV1\logs"
        log_file = os.path.join(log_dir,"Automation_TTD2.log")
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger