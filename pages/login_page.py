from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(Base):
    url = "https://www.hermitageshop.ru/auth/"
    def __init__(self, driver):
        super().__init__(driver)


    """Локаторы"""
    login ="//input[@name='email']"
    password="//input[@name='password']"
    calendar_button="(//button[contains(@class,'MuiIconButton-root')])[1]"
    year_button="//h6[contains(@class,'MuiPickersToolbarText-toolbarTxt')]"
    calendar = "//div[contains(@class,'MuiPickersYear-root') and text()='1991']"
    arrow= "(//button[contains(@class,'MuiButtonBase-root')])[5]"
    select_date="//div[@role='presentation']//button[contains(@class, 'MuiPickersDay-day') and .//text()='15']"
    adress_input="//input[@placeholder='Адрес для доставки']"
    submit_button="//span[contains(@class,'MuiButton-label') and text()='OK']"

    button_enter="//button[@type='submit']"



    """Геттеры"""
    def get_login_input(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_password_input(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_calendar_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.calendar_button)))

    def get_year_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.year_button)))

    def get_arrow(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.arrow)))

    def get_select_date(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_date)))


    # 1991
    def get_calendar(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.calendar)))


    def get_adress_input(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.adress_input)))



    def get_submit_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.submit_button)))

    def get_button_enter(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.button_enter)))


    """Действия"""

    def input_login(self, login):
        self.get_login_input().send_keys(login)
    def input_password(self, password):
        self.get_password_input().send_keys(password)

    def click_calendar_button(self):
        self.get_calendar_button().click()

    def select_calendar(self):
        self.get_calendar()

    def click_year_button(self):
        self.get_year_button().click()

    def click_arrow(self):
        self.get_arrow().click()

    def click_select_date(self):
        self.get_select_date().click()



    def click_submit_button(self):
        self.get_submit_button().click()

    def click_button_enter(self):
        self.get_button_enter().click()

    """Методы"""

    def authorization(self,login, password):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_login(login)
        self.input_password(password)
        self.click_button_enter()




    def click_calendar_buttons(self):
        # self.scroll_to_element(self.get_calendar_button())     # прокрутка
        self.click_with_js(self.get_calendar_button())
        self.click_arrow()
        self.click_select_date()

        self.click_year_button()
        self.scroll_to_element(self.get_calendar())
        self.click_submit_button()


    def input_delivery_address(self, address):
        field = self.get_adress_input()
        field.click()
        self.driver.execute_script("arguments[0].value = '';", field)
        field.send_keys(address)
        field.send_keys(Keys.RETURN)










