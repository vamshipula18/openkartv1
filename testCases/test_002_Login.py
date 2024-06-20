import os
import time

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.Log_Generator import Loggen
from utilities.ReadProperties import ReadConfig


class Test_002_LoginTest:

    def test_login(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        log = Loggen.loggen()
        log.info("*****Testing Login method*****")
        log.info("hitting the url")
        self.driver.get("https://demo.opencart.com/index.php?route=account/logout&language=en-gb")
        self.driver.maximize_window()

        hp = HomePage(self.driver)
        log.info("clicking on my account")
        time.sleep(2)
        hp.clickMyAccount()
        log.debug("clicking on login")
        hp.clickLogin()
        time.sleep(3)
        lp = LoginPage(self.driver)
        log.info("Entering Email")
        lp.enterEmail("vmsht@gmail.com")
        log.info("Entering Password")
        lp.enterPassword("Naruto")
        log.info("clicking on submit")
        lp.clickOnSubmit()
        time.sleep(3)
        log.info("checking if myaccount exists")
        self.targetPage = lp.isMyAccountPageExists()
        if self.targetPage == True:
            assert True
        else:
            path_dir = r"C:\Users\vamsh\PycharmProjects\openKartV1\screenshots"
            screenshot_path = os.path.join(path_dir, "testlogin_ss3.png")
            self.driver.save_screenshot(screenshot_path)
            assert False
        self.driver.close()
        log.info("*****End Of the Login Test*****")
