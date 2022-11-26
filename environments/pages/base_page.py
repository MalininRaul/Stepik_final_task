from selenium.common.exceptions import NoSuchElementException
# добавим конструктор — метод, который вызывается, когда мы создаем объект.
# Конструктор объявляется ключевым словом __init__. В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
# Внутри конструктора сохраняем эти данные как аттрибуты нашего класса. Получается примерно так:
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

# Теперь добавим еще один метод open.
# Он должен открывать нужную страницу в браузере,
# используя метод get()
    def open(self):
        self.browser.get(self.url)

    # напишем вспомогательный метод поиска элемента, который будет возвращать нам True или False
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # метод is_element_present, в котором будем перехватывать исключение. В него будем передавать два аргумента: как искать (css, id, xpath и тд)
    # и собственно что искать (строку-селектор)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True