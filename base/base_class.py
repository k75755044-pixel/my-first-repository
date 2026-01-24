from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Base:
    def __init__(self, driver):
        self.driver = driver


        """Method get current url"""
    def get_current_url(self):
        get_url=self.driver.current_url
        print(f"Наша текущая страница: {get_url}")

    def open(self):
            self.driver.get(self.url)

    """Проверка слова на странице меню"""

    def assert_word(self, element, result):
        value=element.text
        assert value == result
        print(f"Текст корректный: {value}")

    """Прокрутка страницы"""

    def scroll_to_element(self, element):
        WebDriverWait(self.driver, 15).until(EC.visibility_of(element))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def move_to_center(self, element):
        WebDriverWait(self.driver, 15).until(EC.visibility_of(element))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    def moves_to_end(self, element):
        WebDriverWait(self.driver, 15).until(EC.visibility_of(element))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'end'});",
            element
        )




    def click_with_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    """Сравнение цен"""

    def parse_price(self, price_text):
        return int(price_text.replace("₽", "").replace(" ", "").replace("\n", "").strip())




