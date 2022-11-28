from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, "#add_to_basket_form")

class BasketPageLocators():
    PRODUCT_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div') # элемент содержащий сообщение
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1") # элемент содержащий текст сообщения
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong") # элемент содержащий текст сообщения в корзине
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")

