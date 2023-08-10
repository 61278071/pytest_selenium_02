import configparser
Config=configparser.RawConfigParser()
Config.read(r"S:\pycharm_practice_projects\pytest_selenium_02\CONFIGURATIONS\config.ini")
class ReadConfig:
    @staticmethod
    def getURL():
        url=Config.get('common info','url')
        return url
    def getUsername():
        username=Config.get('common info','username')
        return username
    def getPassword():
        password=Config.get('common info','password')
        return password