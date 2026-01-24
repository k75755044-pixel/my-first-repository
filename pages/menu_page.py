from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.login_page import LoginPage


class MenuPage(Base):
    url = "https://www.hermitageshop.ru/lk"

    def __init__(self, driver):
        super().__init__(driver)

        """Локаторы"""

    burger_menu = "//div[contains(@class,'style_Link') and text()='Меню']"
    title="//span[@class='Nav_Nav__Container__title__sT2do'][1]"
    img_aromat= "//img[@src='https://storage.yandexcloud.net/files.hermitageshop/public/37799/conversions/IMG_9722-%283%29_6644cc80a8725-thumb.jpg']"
    word_aromat_for_u= "(//div[@class='style_Label__23FEj'])[110]"

    """Геттеры"""

    def get_burger_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu)))

    def get_title(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, self.title)
            )
        )
    def get_img_aromat(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.img_aromat)))

    def get_word_aromat_for_u(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.word_aromat_for_u)))


    """Действия"""
    # def click_burger_menu(self):
    #     self.get_burger_menu().click()

    def click_element_aromat(self):
        self.get_img_aromat().click()

    def get_aromat_for_u(self):
        self.get_word_aromat_for_u().click()

    def click_burger_menu(self):
        self.get_burger_menu().click()

    """Методы"""



    def enter_main_page_from_menu(self):
        self.click_burger_menu()

    def check_title(self):
        self.assert_word(self.get_title(), "Спецпредложения")

    def move_to_element_aromat(self):
        self.scroll_to_element(self.get_img_aromat())

    def click_aromats_word(self):
        self.get_aromat_for_u()



