
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    lnk_myaccount_xpath = "//i[@class='fa-solid fa-user']"
    lnk_register_linktext = "Register"
    lnk_login_linktext = "Login"
    lnk_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        #wait = WebDriverWait(self.driver,10)
        #wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.lnk_myaccount_xpath))).click()
        self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_register_linktext).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_login_linktext).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_logout_linktext).click()