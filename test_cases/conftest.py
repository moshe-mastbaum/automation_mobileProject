import time
from webdriver_manager.chrome import ChromeDriverManager
import allure
import appium
import pytest
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from utilities.common_ops import get_data, get_timestamp
# from utilities.manage_pages import ManagePages

driver = None
action = None
mobile_size = None


@pytest.fixture(scope='class')
def init_mobile_driver(request):
    globals()['driver']= get_mobile_driver()
    driver=globals()['driver']
    request.cls.driver = driver
    globals()['action'] = TouchAction(driver)
    request.cls.action = globals()['action']
    driver.implicitly_wait(int(get_data('WaitTime')))
    globals()['mobile_size'] = driver.get_window_size()
    request.cls.mobile_size = globals()['mobile_size']
    yield
    time.sleep(3)
    driver.quit()

@pytest.fixture(autouse = True, scope="function")
def fix_function():
    print("\n    Function setup")
    yield
    # driver.start_activity("com.financial.calculator",".FinancialCalculators")
    # driver.start_activity(get_data('app_package'),get_data('app_activity'))
    # driver.execute_script("seetest: client.launch('com.experitest.ExperiBank/.LoginActivity', false, true)")
    driver.press_keycode(4)
    print("\n    Function teardown")

def get_mobile_driver():
    if get_data('mobile_device')=='android':
        driver = get_android()
        return driver
    elif get_data('mobile_device')== 'ios':
        pass
    else:
        driver=None
        raise Exception ('unrecognized mobile device')

def get_android():
    dc={}
    dc['reportDirectory'] = 'c:/appiumproject/appium_reports'
    dc['reportFormat'] = 'xml'
    dc['testName'] = 'test'
    dc['udid'] = get_data('udid')
    dc['appPackage'] = get_data('app_package')
    dc['appActivity'] = get_data('app_activity')
    dc['platformName'] = 'android'
    android_driver = appium.webdriver.Remote(get_data('appium_server'), dc)
    return android_driver

#     catch exceptions, erors
def pytest_exception_interact(node, call, report):
    image = get_data('ScreenshotPath')+'screen'+str(get_timestamp())+'.png'
    globals()['driver'].get_screenshot_as_file(image)
    allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

