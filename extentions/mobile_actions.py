from extentions.ui_actions import UiAction
import test_cases.conftest as conf
import allure
class MobileActions(UiAction):
    @staticmethod
    @allure.tap('tap on element')
    def tap(elem, times):
        conf.action.tap(elem, times)
