
import test_cases.conftest as conf
from page_objects.mobile_obj.calculator_page import CalculatorPage
from page_objects.mobile_obj.currency_page import CurrencyPage
from page_objects.mobile_obj.loan_page import LoanPage
from page_objects.mobile_obj.main_page import MainMobilePage
from page_objects.mobile_obj.stocklist_page import Stocklist

# mobile_objects
from page_objects.mobile_obj.stockreturns_page import Stockreturns

mobile_main = None
mobile_loan = None
mobile_Calculator = None
mobile_currency = None
mobile_stockCalList = None
mobile_stockreturns = None

class ManagePages:
    @staticmethod
    def init_mobile_pages():
        globals()['mobile_main'] = MainMobilePage(conf.driver)
        globals()['mobile_loan'] = LoanPage(conf.driver)
        globals()['mobile_Calculator'] = CalculatorPage(conf.driver)
        globals()['mobile_currency'] = CurrencyPage(conf.driver)
        globals()['mobile_stockCalList'] = Stocklist(conf.driver)
        globals()['mobile_stockreturns'] = Stockreturns(conf.driver)

