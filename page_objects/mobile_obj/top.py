from selenium.webdriver.common.by import By

back = (By.XPATH,"//*[@contentDescription='נווט למעלה']" )

class Top_erea:
    def __init__(self, driver):
            self.driver = driver

    def back(self):
        return self.driver.find_element(back[0], back[1])

