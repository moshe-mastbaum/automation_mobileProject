from selenium.webdriver.common.by import By

loanAmount = (By.XPATH,"//*[@id='loanAmount']" )
interestRate = (By.XPATH,"//*[@id='interestRate']" )
loanYear = (By.XPATH,"//*[@id='loanYear']" )
calculate = (By.XPATH,"//*[@text='CALCULATE']" )
monthlyPayment = (By.XPATH,"//*[@id='monthlyPayment']" )

class LoanPage:
    def __init__(self, driver):
            self.driver = driver

    def loanAmount(self):
        return self.driver.find_element(loanAmount[0], loanAmount[1])
    def interestRate(self):
        return self.driver.find_element(interestRate[0], interestRate[1])
    def loanYear(self):
        return self.driver.find_element(loanYear[0], loanYear[1])
    def calculate(self):
        return self.driver.find_element(calculate[0], calculate[1])
    def monthlyPayment(self):
        return self.driver.find_element(monthlyPayment[0], monthlyPayment[1])

    # def back(self):
    #     return self.driver.find_element(back[0], back[1])
    #
    # self.driver.find_element_by_xpath("xpath=//*[@id='loanAmount']").send_keys('45000')
    # self.driver.find_element_by_xpath("xpath=//*[@id='interestRate']").send_keys('3')
    # self.driver.find_element_by_xpath("xpath=//*[@id='loanYear']").send_keys('5')
    # self.driver.find_element_by_xpath("xpath=//*[@text='CALCULATE']").click()
    # print(self.driver.find_element_by_xpath("xpath=//*[@id='monthlyPayment']").text)