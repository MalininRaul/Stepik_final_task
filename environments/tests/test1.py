from selenium import webdriver
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/")

btn = driver.find_element(By.CSS_SELECTOR, '#add_to_basket_form')
btn.click()

item = driver.find_element(By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
text1 = item.text

basket = driver.find_element(By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
text2 = basket.text

print('Текст в сообщении ', text1)
print('Текст в корзине ',  text2)



#item = driver.find_element(By.)
#print(item)



