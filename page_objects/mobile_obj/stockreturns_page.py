from selenium.webdriver.common.by import By

purchasePrice = (By.XPATH,"//*[@id='purchasePrice']" )
soldPrice = (By.XPATH,"//*[@id='soldPrice']" )
purchaseFee = (By.XPATH,"//*[@id='purchaseFee']" )
soldFee = (By.XPATH,"//*[@id='soldFee']" )
purchased = (By.XPATH,"//*[@text='Purchased']" )
day = (By.XPATH,"//*[@text='1']" )
permision = (By.XPATH,"//*[@text='אישור']" )
soldDate = (By.XPATH,"//*[@id='soldDate']" )
sharesOwned = (By.XPATH,"//*[@id='sharesOwned']" )
calculate = (By.XPATH,"//*[@text='CALCULATE']" )
gainLoss = (By.XPATH,"//*[@id='gainLoss']" )


class Stockreturns:
    def __init__(self, driver):
            self.driver = driver

    def purchasePrice(self):
        return self.driver.find_element(purchasePrice[0], purchasePrice[1])
    def soldPrice(self):
        return self.driver.find_element(soldPrice[0], soldPrice[1])
    def purchaseFee(self):
        return self.driver.find_element(purchaseFee[0], purchaseFee[1])
    def soldFee(self):
        return self.driver.find_element(soldFee[0], soldFee[1])
    def purchased(self):
        return self.driver.find_element(purchased[0], purchased[1])
    def day(self):
        return self.driver.find_element(day[0], day[1])
    def permision(self):
        return self.driver.find_element(permision[0], permision[1])
    def soldDate(self):
        return self.driver.find_element(soldDate[0], soldDate[1])
    def sharesOwned(self):
        return self.driver.find_element(sharesOwned[0], sharesOwned[1])
    def calculate(self):
        return self.driver.find_element(calculate[0], calculate[1])
    def gainLoss(self):
        return self.driver.find_element(gainLoss[0], gainLoss[1])

