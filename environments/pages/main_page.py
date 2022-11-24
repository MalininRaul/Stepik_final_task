#  импорт базового класса BasePage
from .base_page import BasePage
from selenium.webdriver.common.by import By

# Создаем класс  MainPage. Его нужно сделать наследником класса BasePage.
# Класс-предок в Python указывается в скобках
class MainPage(BasePage):
    def go_to_login_page(self): #В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класс
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    #Проверка, есть ли ссылка на логин на странице
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented" #намеренно сделали селектор неправильным, чтобы посмотреть, что именно выдаст тест, если поймает баг