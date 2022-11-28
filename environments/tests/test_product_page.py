from ..pages.product_page import ProductPage
from ..pages.basket_page import BasketPage


def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket() # выполняем метод клика на кнопке Добавить (добавляем продукт и переходим в корзину)
    basket_page = BasketPage(browser, browser.current_url) # получаем текущий url страницы, на которую перешли на предыдущей строке
    basket_page.should_be_basket_page()


#def test_should_be_product_message():
 #   link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
  #  page =



