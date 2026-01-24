import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base



class AromaPage(Base):
    url="https://www.hermitageshop.ru/catalog/cosmetics/foryourself"
    def __init__(self, driver):
        super().__init__(driver)


    """Локаторы"""
    sort_button="//div[@class='style_SortBy__Selector__YqL0b']"
    increase_price= "//div[contains(text(),'возрастанию')]"
    basket= "(//button[contains(@class, 'style_Button') and .//text()='В корзину'])[3]"
    img_cream="//img[@src='https://storage.yandexcloud.net/files.hermitageshop/public/53718/conversions/IMG_1548_6589254da6707-thumb.jpg']"
    icon_basket="//a[@href='/basket']"


    """Геттеры"""
    def get_sort_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.sort_button )))
    def get_increase_price(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.increase_price)))
    def get_basket(self):
        return  WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.basket)))

    def get_img_cream(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.img_cream)))
    def get_icon_basket(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.icon_basket)))



    """Действия"""

    def click_sort_button(self):
        self.get_sort_button().click()
    def click_increase_price(self):
        self.get_increase_price().click()

    def click_basket(self):
        self.get_basket().click()

    def click_icon_basket(self):
        self.get_icon_basket().click()


    """Методы"""

    def sort_price(self):
        self.click_sort_button()
        print("Нажали сортировку")
        self.click_increase_price()
        print("Нажали цена по возрастанию")
        img = self.get_img_cream()
        print("Картинка найдена и прокручена")
        self.moves_to_end(img)

        self.click_basket()
        print("Нажали корзину")

    def add_to_basket(self):
        self.click_icon_basket()
        print("Перешли в корзину")




        time.sleep(5)
