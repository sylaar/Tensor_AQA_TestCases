# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from src.PageObject.Pages.BasePage import BasePage
from src.PageObject.Locators.Locator import Locator


class SabyPage(BasePage):
    '''Класс страницы https://saby.ru/'''

    def click_contacts(self):
        '''
        Находит в хедере элемент "Контакты".
        '''
        self.click_element((Locator.CONTACTS))

    def click_offices_in_the_region(self):
        '''
        Находит ссылку "Еще <> офисов в регионе" в элементе хедера "Контакты" 
         и кликает по ней.
         '''
        self.click_element((Locator.OFFICES_IN_THE_REGION))

    def click_tesnsor_banner(self):
        '''
        Находит баннер Тензор в разделе "Контакты" и кликает по нему.
        После этого переключает фокус на новую вкладку.
        '''
        self.click_element((Locator.TENSOR_BANNER))
        self.driver.switch_to.window(self.driver.window_handles[1])

    def click_current_region(self):
        '''
        Находит выбор текущего региона в разделе "Контакты" 
        и кликает по нему.
        '''
        self.click_element((Locator.CURRENT_REGION))
        
    def click_Kamchatka_region(self):
        '''
        Находит "Камчатский край" в списке регионов раздела "Контакты"
        и кликает по нему.
        '''
        self.click_element((Locator.KAMCHATKA_REGION))

    def get_text_partners_list(self):
        '''
        Находит раздел партнеров в разделе "Контакты".
        Возвращает: город партнеров
        '''
        region_of_partners = self.find_element((Locator.LIST_OF_PARTNERS))
        return region_of_partners.text
    
    def get_text_current_region(self):
        '''
        Находит текущий регион в разделе "Контакты".
        Возвращает: текущий регион
        '''
        current_region = self.find_element((Locator.CURRENT_REGION))
        return current_region.text