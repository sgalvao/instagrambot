from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import PySimpleGUI as sg

<<<<<<< HEAD
VARIANT_GLOBAL_GECKODRIVER = ''

#login = input("Digite seu user:")
#senha = input('digite sua senha:')
#page = input('digite a URL da pagina:')
=======

login = input("Digite seu user:")
senha = input('digite sua senha:')
page = input('digite a URL da pagina:')
>>>>>>> 71dfd81c89f96d2b2a98988246baedab1739f894

class InstagramBot:
    
  

    def __init__(self,login,senha):
        self.username = login
        self.password = senha
<<<<<<< HEAD
        self.driver = webdriver.Firefox(executable_path=VARIANT_GLOBAL_GECKODRIVER) #
=======
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\silvi\\Documents\\geckodriver.exe")
>>>>>>> 71dfd81c89f96d2b2a98988246baedab1739f894


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
        archive = open('wordlist.txt','r')
<<<<<<< HEAD
        comentario =  archive.readlines()#Wordlist
=======
        comentario =  archive.readline()#Wordlist
>>>>>>> 71dfd81c89f96d2b2a98988246baedab1739f894
        driver =self.driver
        driver.get(link)
        driver.find_element_by_class_name('Ypffh').click()
        comment_input = driver.find_element_by_class_name('Ypffh')#campo do comentario
        time.sleep(3)
<<<<<<< HEAD
        i = 0
        for comment in comentario:
            self.typing_method(comment,comment_input)
            comment_button = driver.find_element_by_xpath("//button[@type='submit']")
            comment_button.click()
            time.sleep(40)
            if (i == 5):
                time.sleep(1200)
                i = 0
            else:
                i += 1
            
        



startBot = InstagramBot('accountbottest1', 'bottest123')#Username & password
startBot.login()
startBot.comments('https://www.instagram.com/p/CLNeLh5Fzq8/')#link post
=======
        for i in range(10):
            self.typing_method(random.choices(comentario),comment_input)
            comment_button = driver.find_element_by_xpath("//button[@type='submit']")
            comment_button.click()
            time.sleep(10)



startBot = InstagramBot(login, senha)#Username & password
startBot.login()
startBot.comments(page)#link post
>>>>>>> 71dfd81c89f96d2b2a98988246baedab1739f894
