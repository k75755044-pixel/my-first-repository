from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class OrderPage(Base):
    url="https://www.hermitageshop.ru/ordering"
    def __init__(self, driver):
        super().__init__(driver)

    """Локаторы"""

    field_telephone="//input[@placeholder='Телефон']"
    pickup="//div[contains(@class,'style_Item__') and .//text()='Самовывоз']"
    yandex_map="//div[contains(@class,'style_Title__' )and .//text()='Посещение музея']"
    checkbox_2="//input[@name='get_spam']/ancestor::span[contains(@class,'MuiCheckbox-root')]"
    checkbox_1="//input[@name='agree']/ancestor::span[contains(@class,'MuiCheckbox-root')]"
    confirm_order="//span[contains(@class,'style_Content__') and .//text()='Подтвердить заказ']"
    total_price="//div[contains(@class,'Basket_Basket__TotalPrice__')]"

    """Геттеры"""
    def get_field_telephone(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.field_telephone)))
    def get_pickup(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.pickup)))
    def get_yandex_map(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.yandex_map)))


    def get_checkbox_1(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_1)))
    def get_checkbox_2(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_2)))
    def get_confirm_order(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.confirm_order)))
    def get_total_price(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))


    """Действия"""
    def click_telephone(self,number):
        self.get_field_telephone().send_keys(number)
    def click_pickup(self):
        self.get_pickup().click()

    def click_checkboxes(self):
        self.get_checkbox_1().click()
        self.get_checkbox_2().click()
    def click_confirm_order(self):
        self.get_confirm_order().click()

    def get_price_order_value(self):
        total_price_text = self.get_total_price().text
        return self.parse_price(total_price_text)


    """Методы"""
    def fill_fields(self):

        self.click_telephone("89817076858")
        print("Ввели телефон")
        self.click_pickup()
        print("Нажали самовывоз")
        self.scroll_to_element(self.get_yandex_map())
        print("Сделали скролл")






    def click_checkbox(self):
        self.click_checkboxes()
        print("Нажали чекбоксы")
        self.click_confirm_order()
        print( "Подтвердили заказ")




