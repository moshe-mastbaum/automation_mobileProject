from selenium.webdriver.common.by import By

res = (By.XPATH, "//*[@id='formula']")
btn = (By.XPATH, "//*[@text='", "']" )
class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
    def btn(self, bt):
        return self.driver.find_element(btn[0], btn[1]+bt+btn[2])

    def res(self):
        return self.driver.find_element(res[0], res[1])
