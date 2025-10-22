from selenium.webdriver.common.by import By


class Locator():
    '''Класс с локаторами'''
    CONTACTS = (By.XPATH, '//*[@id="wasaby-content"]/div/div/div/div[2]/div[1]/div[1]\
        /div[1]/div[2]/ul/li[2]/div/div[1]/span')
    OFFICES_IN_THE_REGION = (By.XPATH, '//*[@id="wasaby-content"]/div/div/div/div[2]\
        /div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]/span')
    TENSOR_BANNER = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a\
        /img')
    POWER_IN_PEOPLE = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div')
    MORE_DETAILED = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]\
        /div/p[4]/a')
    WORKING = (By.XPATH, '//div[@class="tensor_ru-About__block3-image-wrapper"]/img')
    CURRENT_REGION = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    KAMCHATKA_REGION = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]\
        /span/span')
    LIST_OF_PARTNERS = (By.XPATH, '//*[@id="city-id-2"]')