from selenium.webdriver.common.by import By

stockreturn = (By.XPATH,"//*[@text='Stock Return and Capital Gain Tax']" )


class Stocklist:
    def __init__(self, driver):
            self.driver = driver

    def stockreturn(self):
        return self.driver.find_element(stockreturn[0], stockreturn[1])
