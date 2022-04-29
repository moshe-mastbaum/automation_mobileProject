
import time
import test_cases.conftest as conf
import utilities.manage_pages as page
from data_driven_test.data1 import data_loan_cal, data_calculator, data_currency, data_stock
from extentions.ui_actions import UiAction
from extentions.verifications import Verifications


class MobileFlows:
    # @staticmethod
    def loan_calculator(self):
        UiAction.click(page.MainMobilePage.loan_cal(self))
        UiAction.text_in(page.LoanPage.loanAmount(self),data_loan_cal['loanAmount'])
        UiAction.text_in(page.LoanPage.interestRate(self),data_loan_cal['interestRate'])
        UiAction.text_in(page.LoanPage.loanYear(self),data_loan_cal['loanYear'])
        UiAction.click(page.LoanPage.calculate(self))
        Verifications.verify_equals(page.LoanPage.monthlyPayment(self).text, data_loan_cal['expected_res'])
        # Verifications.verify_equals(page.LoanPage.monthlyPayment(self).text, 'expected_res')

    def calculator(self):
        print(conf.mobile_size)
        UiAction.click(page.MainMobilePage.calculator(self))
        time.sleep(3)
        UiAction.swipe(700,800,65,800)
        time.sleep(3)
        UiAction.click(page.CalculatorPage.btn(self, data_calculator['cos']))
        UiAction.click(page.CalculatorPage.btn(self, data_calculator['pi']))
        UiAction.swipe(65, 800, 700, 800)
        UiAction.click(page.CalculatorPage.btn(self, data_calculator['divide']))
        UiAction.click(page.CalculatorPage.btn(self, data_calculator['num3']))
        UiAction.click(page.CalculatorPage.btn(self, data_calculator['equal']))
        Verifications.verify_equals(page.CalculatorPage.res(self).text, data_calculator['expected_res'])
        time.sleep(3)

    def currency_converter(self):
        UiAction.click(page.MainMobilePage.currency(self))
        UiAction.click(page.CurrencyPage.fromCurrency(self))
        UiAction.click(page.CurrencyPage.shekel(self))
        UiAction.text_in(page.CurrencyPage.rate(self), data_currency['rate'])
        UiAction.text_in(page.CurrencyPage.amount(self), data_currency['amount'])
        Verifications.verify_equals(page.CurrencyPage.res(self).text, data_currency['expected_res'])

    def test_stock_calculator(self):
        UiAction.click(page.MainMobilePage.stock(self))
        UiAction.click(page.Stocklist.stockreturn(self))
        UiAction.text_in(page.Stockreturns.purchasePrice(self), data_stock['purchasePrice'])
        UiAction.text_in(page.Stockreturns.soldPrice(self), data_stock['soldPrice'])
        UiAction.text_in(page.Stockreturns.purchaseFee(self), data_stock['purchaseFee'])
        UiAction.text_in(page.Stockreturns.soldFee(self), data_stock['soldFee'])
        UiAction.click(page.Stockreturns.purchased(self))
        UiAction.click(page.Stockreturns.day(self))
        UiAction.click(page.Stockreturns.permision(self))
        UiAction.click(page.Stockreturns.soldDate(self))
        UiAction.click(page.Stockreturns.permision(self))
        UiAction.text_in(page.Stockreturns.sharesOwned(self), data_stock['sharesOwned'])
        UiAction.click(page.Stockreturns.calculate(self))
        Verifications.verify_equals(page.Stockreturns.gainLoss(self).text,data_stock['expected_res'])
        self.driver.press_keycode(4)

