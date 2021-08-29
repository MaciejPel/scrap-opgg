from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from os import system, name

# console clear
def clear():
    if name == 'nt': 
        _ = system('cls')  
    else: 
        _ = system('clear')

# info setup
nick='' # nickname
season='' # one of seasons listed below
seasons=['17', '15', '13', '11', '7', '6', '5', '4', '3', '2' ,'1']

# web driver options
options = Options()
options.add_argument('--window-size=1920,1080')
options.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    driver.get('https://eune.op.gg/summoner/champions/userName='+nick)
    driver.find_element_by_xpath("//*[@id='qc-cmp2-ui']/div[2]/div/button[2]").click()
    driver.find_element_by_xpath("//li[contains(@class, 'season-"+season+"')]").click()
    sleep(1.5)
    wins, loses = [], []
    element = driver.find_elements_by_xpath("//div[contains(@class, 'Text') and contains(@class, 'Left')]")
    for i in element:
        temp=i.text.replace('W','')
        if temp:
            wins.append(int(temp))
    element=driver.find_elements_by_xpath("//div[contains(@class, 'Text') and contains(@class, 'Right')]")
    for i in element:
        temp=i.text.replace('L','')
        if temp:
            loses.append(int(temp))
    driver.close()
except Exception as e:
    print(e)
    driver.close()

clear()
print('=== ' + nick + ' season' + season + ' INFO ===')
print('W '+str(sum(wins)))
print('L '+str(sum(loses)))
print('Sum: ' +  str(sum(wins)+sum(loses)))
print(str(round(sum(wins)/(sum(wins)+sum(loses)), 2)*100)+'% WR')