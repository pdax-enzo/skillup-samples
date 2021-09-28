import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class assertElement:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 20)
        self.driver = driver

    def loginPage(self):
        try:
            self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'img[anx-image="sitelogo"]')))
            self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.side-menu-button-li')))
            self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#email")))
            self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#password")))
            self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        except (NoSuchElementException, TypeError):
            pass
        else:
            print("Login Page elements found!")
        finally:
            self.driver.quit()

def startWebDriver(browser, url):
    if browser == "Firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "Chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        sys.exit("Incorrect startWebDriver arguments")
    driver.get(url)
    driver.set_window_size(1920,1080)
    return driver

loginURL = "https://trade.pdax.ph/signin"
wd = startWebDriver("Edge", loginURL)
checkElements = assertElement(wd)
checkElements.loginPage()
