from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=".\\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)
        user_input = driver.find_element_by_xpath("//input[@name='username']")
        user_input.click()
        user_input.clear()
        user_input.send_keys(self.username)
        pass_input = driver.find_element_by_xpath("//input[@name='password']")
        pass_input.click()
        pass_input.clear()
        pass_input.send_keys(self.password)
        pass_input.send_keys(Keys.RETURN)
        time.sleep(3)

    @staticmethod
    def typing_method(phrases,where):
        for letters in phrases:
            where.send_keys(letters)
            time.sleep(random.randint(1,8)/30)

    def comments(self,link):
        for i in range(5):
         comentario = [] #Wordlist
         driver =self.driver
         driver.get("https://www.instagram.com/" + link)
         driver.find_element_by_class_name('Ypffh').click()
         comment_input = driver.find_element_by_class_name('Ypffh')#campo do comentario
         time.sleep(3)
            self.typing_method(random.choice(comentario),comment_input)
            comment_button = driver.find_element_by_xpath("//button[@type='submit']")
            comment_button.click()



startBot = InstagramBot()#Username & password
startBot.login()
startBot.comments()#link post
