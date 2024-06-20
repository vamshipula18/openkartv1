import time

from selenium import webdriver


def test_Check():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    time.sleep(2)