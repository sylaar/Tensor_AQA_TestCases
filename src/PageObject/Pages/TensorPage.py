from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.PageObject.Pages.BasePage import BasePage
from src.PageObject.Locators.Locator import Locator


class TensorPage(BasePage):
    '''Класс страницы https://tensor.ru/'''

    def check_power_in_people_displayed(self):
        '''
        Проверяет видимость блока "Сила в людях".
        '''
        return self.find_element((Locator.POWER_IN_PEOPLE)).is_displayed()
    
    def click_more_detailed(self):
        '''
        Находит в блоке "Сила в людях" ссылку "Подробнее" и кликает по ней.
        '''
        self.click_element((Locator.MORE_DETAILED))

    def get_img_items_working(self):
        '''
        Находит в блоке "Работаем" все изображения.
        Возвращает: список web-элементов всех изображений в этом блоке.
        '''
        images = self.find_elements((Locator.WORKING))
        return images