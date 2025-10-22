import sys
from pathlib import Path
from time import sleep
# добавление пути рабочей директории для дуступа к модулям
abs_path_of_imported_modules = Path(__file__).resolve().parents[2]
sys.path.append(str(abs_path_of_imported_modules))

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from src.WebDriverSetup.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.SabyPage import SabyPage


class TestCaseSecondScript(WebDriverSetup):  

    def test_case_02(self):
        try:
            self.saby_page = SabyPage(self.driver)
            self.driver.get('https://saby.ru/')
            self.saby_page.click_contacts()
            self.saby_page.click_offices_in_the_region()
            assert self.saby_page.get_text_current_region() == 'Ярославская обл.'
            assert self.saby_page.get_text_partners_list() == 'Ярославль'
            self.saby_page.click_current_region()
            self.saby_page.click_Kamchatka_region()
            sleep(1)
            assert 'kamchatskij-kraj' in self.saby_page.get_current_url()
            assert 'Камчатский край' in self.driver.title
            assert self.saby_page.get_text_current_region() == 'Камчатский край'
            assert self.saby_page.get_text_partners_list() == 'Петропавловск-Камчатский'
        except TimeoutException as e:
            print(e)
        finally:
            if self.driver != None:
                self.driver.quit()

if __name__ == '__main__':
    saby_page = TestCaseSecondScript()
    saby_page.test_case_02()