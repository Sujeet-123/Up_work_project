import csv
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


s = Service("/home/zec/Downloads/chromedriver")
driver = webdriver.Chrome(service=s)



df = pd.read_csv('UpWork.csv')

for i in df["Example URL"]:
    driver.get(i)
    driver.maximize_window()
    time.sleep(12)
    

    btn_click = driver.find_element(By.XPATH,'/html/body/ngb-modal-window/div/div/div/div/div[1]/aotf-close-button/button/aotf-icon/span').click() 

    # Address = driver.find_element(By.XPATH,'//*[@id="main-content"]/div[2]/aotf-property-header/section/address/p[2]')
    Address = driver.find_element(By.CLASS_NAME,'address-line-one');time.sleep(5) 
    print(Address.text)

    # priceDiv = driver.find_element(By.CLASS_NAME,'inner-content.desktop-monthly')
    # price = priceDiv.find_element(By.CLASS_NAME,'price').text

    # M_price_1 = priceDiv.find_element(By.XPATH,'//*[@id="main-content"]/div[2]/section[1]/div/div/div[2]/aotf-property-detail-card/div/div/div/div[1]/span/span[2]').text

    # content = driver.find_element(By.XPATH,'//*[@id="main-content"]/div[2]/section[1]/div/div/div[1]/aotf-general-info/div/div').text
    # print(price)
    # print(M_price_1)
    # print(content)
 
    # driver.execute_script('scrollTo(0,700)')

    # F_t = driver.find_elements(By.XPATH,'//*[@id="main-content"]/div[2]/section[1]/div/div/aotf-feature-list/ul/li[*]')
    # for j in F_t:
    #     print(j.text)
    #     time.sleep(2)


    # clk = driver.find_element(By.XPATH,'//*[@id="main-content"]/div[2]/section[2]/section[1]/aotf-collapsible/div/h2/button/aotf-icon/span').click();time.sleep(3)

    # property = driver.find_elements(By.XPATH,'//*[@id="collapsible-zeoc1o40hm"]/div/aotf-property-details[1]/dl/dt')
    
    # driver.execute_script('scrollTo(0,500)')
    # for k in property:
    #     print("++++++++++++for++++++++++++++++++")
    #     print(k.text)
    #     time.sleep(2)



    break



