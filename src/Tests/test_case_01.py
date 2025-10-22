import sys
from pathlib import Path
from time import sleep

# добавление пути рабочей директории для дуступа к модулям
abs_path_of_imported_modules = Path(__file__).resolve().parents[2]
sys.path.append(str(abs_path_of_imported_modules))

from selenium.common.exceptions import TimeoutException

from src.WebDriverSetup.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.SabyPage import SabyPage
from src.PageObject.Pages.TensorPage import TensorPage


class TestCaseFirstScript(WebDriverSetup):

    def test_case_01(self):
        try:
            self.saby_page = SabyPage(self.driver)
            self.tensor_page = TensorPage(self.driver)  
            self.driver.get('https://saby.ru/')
            self.saby_page.click_contacts()
            self.saby_page.click_offices_in_the_region()
            self.saby_page.click_tesnsor_banner()
            sleep(1)
            assert self.tensor_page.check_power_in_people_displayed()
            self.tensor_page.click_more_detailed()
            images = self.tensor_page.get_img_items_working()
            image_dimensions = [] # список словарей с размерами изображения
            for image in images:
                height = image.get_attribute('height')
                width = image.get_attribute('width')
                image_dimensions.append({'height': height, 'width': width})
            first_dimension = image_dimensions[0] # размеры первого изображения
            assert all(dimension == first_dimension for dimension in image_dimensions)
            self.tensor_page.get_current_url() == 'https://tensor.ru/about'
        except TimeoutException as e:
            print(e)
        finally:
            if self.driver != None:
                self.driver.quit()

if __name__ == '__main__':
    test = TestCaseFirstScript()
    test.test_case_01()