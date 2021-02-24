from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import getpass




diretory = input('Passe o diretorio do Geckodriver:')
login = input("Digite seu user:")
senha = getpass.getpass('digite sua senha:')
page = input('digite a URL da pagina:')

class InstagramBot:
    in feina ksdkl ksdijw3s
  

    def __init__(self,login,senha):
        self.username = login
        self.password = senha
        self.driver = webdriver.Firefox(executable_path='C://users//silvi//documents//geckodriver.exe') #geckodriver


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
        time.sleep(3)
        i = 1
        contador = 1
        while True: 
            driver.find_element_by_class_name('Ypffh').click()
            comment_input = driver.find_element_by_class_name('Ypffh')
            time.sleep(3)
            controller = []
            controller.extend(comentario)
            del comentario[:2]
            self.typing_method(controller[0],comment_input)
            self.typing_method(controller[1],comment_input)
            comment_button = driver.find_element_by_xpath("//button[@type='submit']")
            comment_button.click()
            try:
                time.sleep(2)
                driver.find_element_by_class_name('gxNyb')
                #driver.find_element_by_xpath("//button[contains(text(), 'Tentar novamente')]")
                #tryAgain.click()
                driver.refresh()
                contador -= 1
                i -= 1
                print(controller[0], controller[1],' ###ERROR###')
            except:
             print(controller[0], controller[1],) 
             print('Comentario publicado:', contador) #acrescentar 287 na soma de comentarios.
             time.sleep(random.randint(30,45))
            if (i == 50):
                
                time.sleep(random.randint(3600, 3700))
                i = 1
            else:
                 i += 1 
                 contador += 1          
        


startBot = InstagramBot(login, senha )#Username & password
startBot.login()
startBot.comments(page)#link post

# Traceback (most recent call last):
#   File "C:\Users\silvi\Desktop\BotInsta\BotIg.py", line 88, in <module>
#     startBot.login()
#   File "C:\Users\silvi\Desktop\BotInsta\BotIg.py", line 55, in comments
#     driver.find_element_by_class_name('Ypffh').click()
#   File "C:\Users\silvi\AppData\Local\Programs\Python\Python39\lib\site-packages\selenium\webdriver\remote\webelement.py", line 80, in click
#     self._execute(Command.CLICK_ELEMENT)
#   File "C:\Users\silvi\AppData\Local\Programs\Python\Python39\lib\site-packages\selenium\webdriver\remote\webelement.py", line 633, in _execute
#     return self._parent.execute(command, params)
#   File "C:\Users\silvi\AppData\Local\Programs\Python\Python39\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
#     self.error_handler.check_response(response)
#   File "C:\Users\silvi\AppData\Local\Programs\Python\Python39\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
#     raise exception_class(message, screen, stacktrace)
# selenium.common.exceptions.ElementClickInterceptedException: Message: Element <textarea class="Ypffh focus-visible"> is not clickable at point (908,627) because another element <form class="X7cDz"> obscures it


# <div class="CgFia "><div class="HGN2m XjicZ"><div class="JBIyP"><p class="gxNyb">Não foi possível publicar o comentário.</p></div><button class="sqdOP yWX7d    y3zKF     " type="button">Tentar novamente</button></div></div>