
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pandas as pd




s = Service("/home/zec/Downloads/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get('https://resanfrancisco.rapmls.com/scripts/mgrqispi.dll?APPNAME=REsanfrancisco&PRGNAME=MLSLogin&ARGUMENT=hBgsIMRP+yPlxRRSP8peaLFENPgFydCOA+2xw90X1KGIaDmUGEJejXo69HWYP1Wb&KeyRid=1&ClientPortalAgentNumber=1075241')
time.sleep(5)
driver.maximize_window()
time.sleep(5)



Address_1 = []
Price_1 = []
Description_1 = []
Monthly_Rent_1 = []
Beds_1 = []
Baths_1 = []





add = driver.find_element(By.XPATH,'//*[@id="Workspace"]/table/tbody/tr/td/form[2]/table[1]/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/span[1]').text
print('address => ',add)
Address_1.append(add)

driver.find_element(By.XPATH,'//*[@id="Remarks"]/div[1]/a').click()

discribtion = driver.find_element(By.XPATH,'//*[@id="Remarks"]/div[2]').text
print("discribtion => ",discribtion)
Description_1.append(discribtion)

price = driver.find_element(By.XPATH,'//*[@id="Workspace"]/table/tbody/tr/td/form[2]/table[1]/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[1]/span[2]').text
print('price => ',price)
Price_1.append(price)

bedrooms = driver.find_element(By.XPATH,'//td/span[@class="mBlackText"]').text
bed = bedrooms.split(':')[1]
print('bedroom => ', bed)
Beds_1.append(bed)      

bathrooms = driver.find_element(By.XPATH,'//*[@id="Workspace"]/table/tbody/tr/td/form[2]/table[1]/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]/span').text
bath = bathrooms.split(':')[1]
print('bathroom => ',bath)
Baths_1.append(bath)

rent = driver.find_element(By.XPATH,'//*[@id="Workspace"]/table/tbody/tr/td/form[2]/table[1]/tbody/tr/td/table/tbody/tr[80]/td[2]').text
print("Rent => ",rent)
Monthly_Rent_1.append(rent)


Dic = {
    'Address':Address_1,
    'Price':Price_1,
    'Beds':Beds_1,
    'Baths':Baths_1,
    'Description': Description_1,
    'Monthly_Rent':Monthly_Rent_1


}

df = pd.DataFrame(Dic)
print(df)
     