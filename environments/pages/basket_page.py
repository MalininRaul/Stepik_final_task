from .base_page import BasePage
from ..pages.locators import BasketPageLocators

class BasketPage(BasePage, BasketPageLocators):
    def should_be_basket_page(self):
        self.should_be_product_message()
        self.should_be_content_product_message()
        #self.should_be_price_message()
       #self.should_be_content_price_message()

    def should_be_product_message(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_MESSAGE), "Product message is not presented"

    def should_be_content_product_message(self):
        product_name = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET_MESSAGE).text
        print(product_name, message)
        assert product_name == message, 'Name is not equal'

    def should_be_right_price(self):
        product_price = self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*BasketPageLocators.BASKET_PRICE).text
        print(product_price, basket_price)
        assert product_price == basket_price, f"{product_price} not equal {basket_price}"

