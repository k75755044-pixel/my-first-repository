from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class BasketPage(Base):
    url = "https://www.hermitageshop.ru/basket"
    def __init__(self, driver):
        super().__init__(driver)

    """Локаторы"""
    ordering="//a[@href='/ordering']"
    price_order="//div[contains(@class,'style_Total__Price')]"

    """Геттеры"""
    def get_ordering(self):
        return  WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.ordering)))
    def get_price_order(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.price_order)))

    """Действия"""

    def click_ordering(self):
        self.get_ordering().click()

    def get_price_order_value(self):
        basket_price_text = self.get_price_order().text
        return self.parse_price(basket_price_text)

    """Методы"""

    def click_order(self):
        self.click_ordering()
