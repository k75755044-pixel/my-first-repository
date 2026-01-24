from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class MainPage(Base):
    url = "https://www.hermitageshop.ru/"
    def __init__(self, driver):
        super().__init__(driver)

    """Локаторы"""
    lk_link="(//button[@class='style_Action__1id1K style_Action_white__dAkV4'])[2]"
    """Геттеры"""
    def get_lk_link(self):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.lk_link )))

    """Действия"""

    def click_lk_link(self):
        self.get_lk_link().click()

    """Методы"""

    def click_login_link(self):
        self.click_lk_link()

