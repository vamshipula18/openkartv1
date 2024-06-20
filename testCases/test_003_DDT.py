import time

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.Log_Generator import Loggen
from utilities.ReadProperties import ReadConfig
from utilities.XLutils import XLutils


class Test_003_DataDriven:
    def test_003_DDT(self, setup):
        self.driver = setup
        log = Loggen.loggen()
        file_path = r"C:\Users\vamsh\PycharmProjects\openKartV1\testData\DataDriven.xlsx"
        self.driver.implicitly_wait(5)
        url = ReadConfig.getApplicationURL()
        log.info("Hitting the Application")
        self.driver.get(url)
        self.driver.maximize_window()
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        xl = XLutils()
        log.debug("Clicking on MyAccount")
        time.sleep(1)
        hp.clickMyAccount()
        time.sleep(3)
        log.info("Clicking on login")
        hp.clickLogin()
        self.rows = xl.getRowCount(file_path, "Sheet1")
        lst_status = []

        for r in range(2, self.rows+1):
            self.email = xl.readData(file_path, "Sheet1", r, 1)
            self.password = xl.readData(file_path,"Sheet1", r, 2)
            self.expected = xl.readData(file_path, "Sheet1", r, 3)
            log.info("Entering email")
            time.sleep(2)
            lp.enterEmail(self.email)
            log.info("Entering Password")
            lp.enterPassword(self.password)
            lp.clickOnSubmit()
            log.info("Checking is My Account Page Exists")
            self.target = lp.isMyAccountPageExists()
            if self.expected == "Valid":
                if self.target == "True":
                    lst_status.append("Pass")
                    log.info("clicking on logout after succesfull login")
                    time.sleep(2)
                    hp.clickLogout()
                else:
                    lst_status.append("Fail")
            elif self.expected == "Invalid":
                if self.target == "True":
                    lst_status.append("Fail")
                    hp.clickLogout()
                else:
                    lst_status.append("Pass")

            self.driver.refresh()
        print(lst_status)
        self.driver.close()

        #final Validation:
        log.info("Checking lst_status ")
        if "Fail" not in lst_status:
            assert True
        else:
            assert False



