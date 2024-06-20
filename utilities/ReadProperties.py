import os
import configparser

path = r"C:\Users\vamsh\PycharmProjects\openKartV1\configurations"
config = configparser.ConfigParser()
config.read(os.path.join(path,"config.ini"))

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=(config.get('commonInfo', 'baseURL'))
        return url


#Testing above methods - optional Code
print(ReadConfig.getApplicationURL())
