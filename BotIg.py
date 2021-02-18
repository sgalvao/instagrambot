from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import PySimpleGUI as sg
import getpass

VARIANT_GLOBAL_GECKODRIVER = 'C:\\Users\\silvi\\Documents\\geckodriver.exe'

login = input("Digite seu user:")
senha = getpass.getpass('digite sua senha:')
page = input('digite a URL da pagina:')

class InstagramBot:
    
  

    def __init__(self,login,senha):
        self.username = login
        self.password = senha
        self.driver = webdriver.Firefox(executable_path=VARIANT_GLOBAL_GECKODRIVER) #geckodriver


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
        comentario =  archive.readlines()#Wordlist
        driver =self.driver
        driver.get(link)
        #driver.find_element_by_class_name('Ypffh').click()
        #comment_input = driver.find_element_by_class_name('Ypffh')#campo do comentario
        time.sleep(3)
        i = 0
        while True: 
            driver.find_element_by_class_name('Ypffh').click()
            comment_input = driver.find_element_by_class_name('Ypffh')
            time.sleep(3)
            controller = []
            controller.extend(comentario)
            del comentario [:2]
            self.typing_method(controller[0],comment_input)
            self.typing_method(controller[1],comment_input)
            comment_button = driver.find_element_by_xpath("//button[@type='submit']")
            comment_button.click()
            time.sleep(2)
            driver.refresh()
            time.sleep(35)
            if (i == 35):
                time.sleep(3600)
                i = 0
            else:
                i += 1
            
        



startBot = InstagramBot(login, senha )#Username & password
startBot.login()
startBot.comments(page)#link post
