from selenium.webdriver.common.by import By


class LoginPage:

    txt_Email_Xpath = "//input[@name='email']"
    txt_Password_Xpath = "//input[@name='password']"
    lnk_submit_Css = "button[type='submit']"
    txt_MyAccount_Xpath = "//h2[text()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def enterEmail(self, email):
        return self.driver.find_element(By.XPATH, self.txt_Email_Xpath).send_keys(email)

    def enterPassword(self, password):
        return self.driver.find_element(By.XPATH, self.txt_Password_Xpath).send_keys(password)

    def clickOnSubmit(self):
        self.driver.find_element(By.CSS_SELECTOR, self.lnk_submit_Css).click()

    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_MyAccount_Xpath).is_displayed()
        except:
            return False

