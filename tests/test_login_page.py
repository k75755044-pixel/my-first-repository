import time

from selenium import webdriver

from pages.aromats_page import AromaPage
from pages.basket_page import BasketPage
from pages.card_page import CardPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.menu_page import MenuPage
from pages.order_page import OrderPage


def test_login_page():
    driver = webdriver.Chrome()
    driver.get("https://www.hermitageshop.ru/")
    lk=MainPage(driver)
    lk.open()
    lk.click_login_link()

    login = LoginPage(driver)
    login.open()
    login.authorization("kamkamila@bk.ru","KBW7Zg9wDqg4CfH")
    time.sleep(1)
    login.click_calendar_buttons()
    login.input_delivery_address("Санкт Петербург, улица Кораблестроителей 7")
    time.sleep(2)



    mp=MenuPage(driver)
    mp.enter_main_page_from_menu()
    time.sleep(1)
    mp.get_current_url()
    mp.check_title()
    mp.move_to_element_aromat()
    mp.click_aromats_word()

    ap=AromaPage(driver)
    ap.open()
    ap.sort_price()
    ap.add_to_basket()

    bp=BasketPage(driver)
    bp.open()
    price_order=bp.get_price_order_value()
    bp.click_order()

    op=OrderPage(driver)
    op.open()
    total_price=op.get_price_order_value()
    op.fill_fields()
    op.click_checkbox()

    assert price_order == total_price
    print(f"Цена в корзине {price_order} и цена в оформлении заказа {total_price} совпадают")

    cp=CardPage(driver)
    cp.open()
    cp.fill_info_card()




    print("GOOD")





    time.sleep(10)
