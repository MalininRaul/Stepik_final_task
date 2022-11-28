from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasketPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add = self.browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form")
        button_add.click()

    # проверка, есть ли кнопка Добавить на странице
    #def should_be_button_add(self):
     #   assert self.is_element_present(*ProductPageLocators.BUTTON_ADD), "Button_add is not presented"

# проверка, что сообщение появилось
    def should_be_basket_page(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_MESSAGE), "Product message is not presented"
# проверка, что наименование в сообщении соответствует товару в корзине
# проверка, что сообщение о цене появилось
# проверка, что цена в сообщении соответствует цене в корзине