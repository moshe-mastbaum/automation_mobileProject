from selenium.webdriver.common.by import By

loan_cal = (By.XPATH,"//*[@text='Loan Calculator']" )
calculator = (By.XPATH,"//*[@text='Calculator']" )
currency = (By.XPATH,"//*[@text='Currency Converter']" )
stock = (By.XPATH,"//*[@text='Stock Calculator']" )

class MainMobilePage:
    def __init__(self, driver):
            self.driver = driver

    def loan_cal(self):
        return self.driver.find_element(loan_cal[0], loan_cal[1])
    def calculator(self):
        return self.driver.find_element(calculator[0], calculator[1])
    def currency(self):
        return self.driver.find_element(currency[0], currency[1])
    def stock(self):
        return self.driver.find_element(stock[0], stock[1])