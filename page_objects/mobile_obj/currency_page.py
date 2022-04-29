from selenium.webdriver.common.by import By

fromCurrency = (By.XPATH, "//*[@id='fromCurrencySpinner']")
shekel = (By.XPATH, "//*[@text='Israeli Shekel:ILS']")
rate = (By.XPATH, "//*[@id='exchRateInput']")
amount = (By.XPATH, "//*[@id='amountInput']")
res = (By.XPATH, "//*[@id='converterResult']")


class CurrencyPage:
    def __init__(self, driver):
        self.driver = driver

    def fromCurrency(self):
        return self.driver.find_element(fromCurrency[0], fromCurrency[1])

    def shekel(self):
        return self.driver.find_element(shekel[0], shekel[1])

    def rate(self):
        return self.driver.find_element(rate[0], rate[1])

    def amount(self):
        return self.driver.find_element(amount[0], amount[1])

    def res(self):
        return self.driver.find_element(res[0], res[1])
