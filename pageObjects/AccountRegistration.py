from selenium.webdriver.common.by import By


class AccountRegistration:
    txt_firstname_xpath = "//input[@name='firstname']"
    txt_lastname_id = "input-lastname"
    txt_email_id = "input-email"
    txt_password_id = "input-password"
    chk_policymaker_name = "agree"
    btn_continue_css = "button[type='submit']"
    txt_message_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, name):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(name)

    def setLastName(self, lastName):
        self.driver.find_element(By.ID, self.txt_lastname_id).send_keys(lastName)

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def setPolicyAgree(self):
        self.driver.find_element(By.NAME, self.chk_policymaker_name).click()

    def setContinue(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_continue_css).click()

    def successText(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_message_xpath).text
        except:
            None

