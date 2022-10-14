
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s = Service("/home/zec/Downloads/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get('https://matrix.brightmls.com/DAE.asp?ID=0-4160670010-10&eml=amFrZUBqc3F1YXJlZDJsbGMuY29t&rk=1346975474')

time.sleep(10)


print('=================================================')

WebDriverWait(driver, 10).until(EC.alert_is_present())
driver.switch_to.alert.accept()
time.sleep(10)

driver.maximize_window()
time.sleep(8)

print('========================123=========================')






Address_1 = []
# Address_2 = []
Price_1 = []
Property_taxes_1 = []
Beds_1 = []
Baths_1 = []
Unit_number_1 = []

Description_1 = []

clr = driver.find_element(By.XPATH,'//*[@id="wrapperTable"]/div/div[2]/div[2]/div[1]/span/a')
clr.click()
time.sleep(5)

for i in range(1,57):

    try:    
        addDiv = driver.find_element(By.CLASS_NAME,'d-mega.d-fontSize--mega.d-color--brandDark.col-sm-12')
        add = addDiv.find_element(By.TAG_NAME,'a').text
        Address_1.append(add)
        print('add => ',add)
    except:
        Address_1.append("No data")

    # add2 = driver.find_element(By.XPATH,'//*[@id="wrapperTable"]/div/div/div[1]/div[1]/div/div[2]/span').text
    # print('add2 => ',add2)
    try:
        price = driver.find_element(By.XPATH,'//*[@id="wrapperTable"]/div/div/div[5]/div/div/div[1]/div/div[2]/span').text
        print('price => ',price)
        Price_1.append(price)
    except:
        Price_1.append("No data")

    try:
        annual_tax_amount = driver.find_element(By.XPATH,'//*[@id="wrapperTable"]/div/div/div[6]/div/div[3]/div/div[2]/div/div[3]/div/div[6]/div/div/div[1]/div/div[2]/span').text
        print('annual_tax_amount => ',annual_tax_amount)
        Property_taxes_1.append(annual_tax_amount)
    except:
        Property_taxes_1.append("No data")
    #numbers of unit
    try:
        building_units_total = driver.find_element(By.XPATH,'//*[@id="wrapperTable"]/div/div/div[6]/div/div[3]/div/div[2]/div/div[3]/div/div[20]/div/div/div[1]/div/div[2]/span').text
        print('building_units_total => ',building_units_total)
        Unit_number_1.append(building_units_total)
    except:
        print("expect building_units_total")
        Unit_number_1.append("No data")

    try:

        description = driver.find_element(By.XPATH,'//*[@id="wrapperTable"]/div/div/div[3]/div[1]/div[1]/div/span').text
        print('description => ',description)
        Description_1.append(description)
        
    except:
        Description_1.append("No data")

    
    try:
        obu = driver.find_element(By.XPATH,'//*[@id="wrapperTable"]/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/span[1]').text
        print('One Bedroom Units => ',obu)
        Beds_1.append(obu)
    except:
        Beds_1.append("No data")

    try:
        bath = driver.find_element(By.XPATH,'//*[@id="wrapperTable"]/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[3]/span[1]').text 
        print('Bathroom unit =>',bath)
        Baths_1.append(bath)

    except:
        print("except Bathroom unit")
        Baths_1.append("No data")




    driver.find_element(By.CLASS_NAME,'glyphicon.glyphicon-chevron-right ').click()
    time.sleep(10)



Dic = {
    'Address':Address_1,
    'Price':Price_1,
    'Property_taxes':Property_taxes_1,
    'Beds':Beds_1,
    'Baths':Baths_1,
    'Unit_number':Unit_number_1,
    'Description': Description_1

}

df = pd.DataFrame(Dic)
print(df)
     