import logging

class LogGen:
    @staticmethod
    def loggen():
        logger=logging.getLogger('test_logger')
        logger.setLevel(logging.INFO)
        file_handle=logging.FileHandler("S:\\pycharm_practice_projects\\pytest_selenium_02\\Logs\\automation.log")
        #file format=[DataTime, Level, Message], for DataTime format use datafmt argument
        file_format=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%m%d%Y %I:%M:%S %p')
        file_handle.setFormatter(file_format)
        logger.addHandler(file_handle)
        return logger