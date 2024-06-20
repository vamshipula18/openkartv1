import os
import time

from pageObjects.AccountRegistration import AccountRegistration
from pageObjects.HomePage import HomePage
from utilities import randomString
from utilities.Log_Generator import Loggen
from utilities.ReadProperties import ReadConfig


class Test_001_AccountReg:


    def test_AccountReg(self, setup):

        self.driver = setup
        log = Loggen.loggen()
        log.info("***Start of test_AccountReg***")
        self.driver.implicitly_wait(15)
        self.baseURL = ReadConfig.getApplicationURL()
        log.info("hitting the url")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        log.info("clicking on myaccount")
        time.sleep(2)
        self.hp.clickMyAccount()
        log.info("clicking on register")
        time.sleep(2)
        self.hp.clickRegister()
        self.ar = AccountRegistration(self.driver)
        log.info("setting the firstname")
        self.ar.setFirstName("Takashi")
        log.info("setting the last name")
        self.ar.setLastName("hama")
        #self.email = randomString.random_string_generator(5)+"@gmail.com"
        log.info("entering email")
        self.ar.setEmail("vamshipula@gmail.com")
        log.info("setting password")
        self.ar.setPassword("vamshiPula")
        time.sleep(2)
        log.info("clicking on privacy policy")
        self.ar.setPolicyAgree()
        time.sleep(2)
        log.debug("clicking one continue")
        self.ar.setContinue()
        time.sleep(3)
        self.confirmcheck = self.ar.successText()
        print(self.confirmcheck)
        log.info("checking the success message")
        if self.confirmcheck == "Your Account Has Been Created!":
            self.hp.clickMyAccount()
            self.hp.clickLogout()
            assert True

        else:
            # Get the current directory
            current_directory = r"C:\Users\vamsh\PycharmProjects\openKartV1\screenshots"
            # Define the path for saving the screenshot
            screenshot_path = os.path.join(current_directory, "reg_ss1.png")
            # Save the screenshot
            self.driver.save_screenshot(screenshot_path)
            assert False
        self.driver.close()
        log.info("***End of Test_AccountReg***")
