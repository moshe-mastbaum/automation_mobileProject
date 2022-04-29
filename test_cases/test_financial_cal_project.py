import time
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_cases.conftest import driver
from workfows.mobile_flows import MobileFlows


@pytest.mark.usefixtures('init_mobile_driver')
class Test_Others:

    def test_loan_cal1(self):
        MobileFlows.loan_calculator(self)

    def test_math_trigo_cal2(self):
        MobileFlows.calculator(self)

    def test_converter3(self):
        MobileFlows.currency_converter(self)

    def test_stock4(self):
        MobileFlows.test_stock_calculator(self)

   












