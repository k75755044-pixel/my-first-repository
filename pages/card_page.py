from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CardPage(Base):
    url="https://secure.ypmn.ru/pay/v2/"
    def __init__(self, driver):
        super().__init__(driver)

    """Локаторы"""
    card_number="//input[@class='input card-number']"
    month_year="//input[@id='cc_exp_full']"
    cvv="//input[@class='input cvv']"
    payment_button="//a[@id='complete-payment']"
    """Геттеры"""
    def get_card_number(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.card_number)))
    def get_month_year(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.month_year)))
    def get_cvv(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.cvv)))
    def get_payment_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.payment_button)))

    """Действия"""
    def input_get_card_number(self,numbers):
        self.get_card_number().send_keys(numbers)
    def input_month_year(self,month_year):
        self.get_month_year().send_keys(month_year)
    def input_cvv(self,cvv):
        self.get_cvv().send_keys(cvv)
    def input_payment_button(self):
        self.get_payment_button().click()

    """Методы"""
    def fill_info_card(self):
        self.input_get_card_number("4111111111111111")
        print("Ввели номер карты")
        self.input_month_year("12/30")
        print("Ввели месяц/год")
        self.input_cvv("123")
        print("Ввели cvv")
        self.input_payment_button()
        print("Нажали оплатить")