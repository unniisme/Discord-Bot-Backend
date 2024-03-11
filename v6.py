from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import settings
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

s= Service('chromedriver.exe')
driver=uc.Chrome()

def Login():
    driver.get('https://leetcode.com/accounts/login/')
    time.sleep(5)
    
    login=driver.find_element(by=By.XPATH,value="//input[@name='login']")
    password=driver.find_element(by=By.XPATH,value="//input[@name='password']")
    time.sleep(3)
    login.send_keys(settings.Username)
    time.sleep(3)
    password.send_keys(settings.Password)
    time.sleep(3)
    login_but=driver.find_element(by=By.XPATH,value="//button[@id='signin_btn']")
    login_but.click()
    time.sleep(7)


def Get_Answers():
    #Click on solution tab
    time.sleep(5)
    element = driver.find_element(by=By.XPATH,value="//div[@class='normal absolute left-0 top-0 whitespace-nowrap font-normal' and text()='Solutions']")
    element.click()
    #Once in solution tab
    def ParseLanguages(set_word):
            languages=[]
            lang=["Java","Python","C","JavaScript","Go","TypeScript","Rust","Kotlin","PHP","Ruby","Swift","Dart","Scala","Elixir","Racket","Erlang","MySQL"]
            
            for line in set_word:
                    for word in line.split('\n'):
                        if word != '':
                            if word in ["Python3","Python ML"]:
                                languages.append("language-python")
                            elif word=="C#":
                                languages.append("language-csharp")
                            elif word=="C++":
                                languages.append("language-cpp")
                            elif word in lang:
                                languages.append("language-"+word.lower())
            return languages 
    #Get all the languages
    time.sleep(5)
    parent=driver.find_element(by=By.XPATH,value="//div[@class='flex w-full flex-col']")
    first_child=parent.find_element(by=By.XPATH,value="./*[1]")
    lang=first_child.find_elements(by=By.XPATH,value=".//div[@class='text-label-2 dark:text-dark-label-2 bg-fill-3 dark:bg-dark-fill-3 whitespace-nowrap rounded-[20px] px-2 py-[1px] text-xs']")
    Languages=set()
    for i in lang:
            Languages.add(i.get_attribute("innerText"))
    Languages=ParseLanguages(Languages)
    first_child.click()
    time.sleep(5)
    #The part responsible for answers in solution page
    button=driver.find_elements(by=By.XPATH,value="//*[@class='relative cursor-pointer px-3 py-3 text-label-4 dark:text-dark-label-4 hover:text-label-1 dark:hover:text-dark-label-1 EoHqa']")
    for element in button:
            print('Clicking the button')
            element.click()
            time.sleep(2)
    
    for j in Languages: 
        code=driver.find_elements(by=By.XPATH,value=f"//code[@class='{j}']")
        with open('Answers.txt','a') as file:
            file.write("\n\n")
            file.write(f"-----------{j}-----------------\n")
            for i in code:
                file.write(i.get_attribute("innerText"))
                file.write("\n")

def Get_Question():
    time.sleep(5)
    element= driver.find_element(by=By.XPATH,value="//div[@data-track-load='description_content']")
    with open('Questions.txt','a',encoding='utf-8') as file:
        file.write(element.get_attribute('innerText'))
        file.write('\n')

def Get_Urls():
    titles=[]
    cleaned_title=[]
    elements = driver.find_elements(by=By.XPATH,value="//td[@label='Title']")
    for element in elements:
        title = element.get_attribute("value")
        titles.append(title)
    
    for line in titles:
        url=f"https://leetcode.com/problems/{'-'.join(line.split())}/"
        cleaned_title.append(url)
    
    return cleaned_title


Login()
driver.get("https://leetcode.com/tag/counting-sort/")
time.sleep(5)
cleaned_title = Get_Urls()
for url in cleaned_title:
    driver.get(url)
    Get_Question()
    Get_Answers()
    time.sleep(2)