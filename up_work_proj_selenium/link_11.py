from gettext import find
from lib2to3.pgen2.driver import Driver
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


s = Service("/home/zec/Downloads/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get('https://mandrillapp.com/track/click/30721448/www.roofstock.com?p=eyJzIjoicmRvYTZEZlNlOHRveWlTWmJVZmYwczFqYTZrIiwidiI6MSwicCI6IntcInVcIjozMDcyMTQ0OCxcInZcIjoxLFwidXJsXCI6XCJodHRwczpcXFwvXFxcL3d3dy5yb29mc3RvY2suY29tXFxcL2ludmVzdG1lbnQtcHJvcGVydHktZGV0YWlsc1xcXC8xOTg0Njc3P3V0bV9zb3VyY2U9cm9vZnN0b2NrJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPXJlY2VudF9maWx0ZXJcIixcImlkXCI6XCI0MjI3N2YxZjFhMjA0YjhkYTdjYmUzODQ0MjhiYWYzMVwiLFwidXJsX2lkc1wiOltcIjY0MWZhM2MzZWIwYTkyZjJhMDZhNTg5ZDk3NWFiMTJhOGI1MTc0YzlcIl19In0')
driver.maximize_window()
time.sleep(8)
# time.sleep(5)

driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div/button').click()
time.sleep(8)

Address_1 = []
Address_2 = []
Price_1 = []
Monthly_Rent_1 = []
Property_taxes_1 = []
Beds_1 = []
Baths_1 = []

divs = driver.find_elements(By.CLASS_NAME,'RoofCardV2style__BottomBarStyled-sc-xlmarl-3.eURsya')

# for j in range(1,90):
n = 0

for i in range(1,len(divs)+4):



    if i == 5 or i == 12 or i == 18:
        pass
    else:


        l = driver.find_element(By.XPATH,f'/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/div[{i}]/div/a/div[1]/div[1]/div/div/div[2]/div/div[2]/div/div/img')
        # l = driver.find_element(By.CLASS_NAME,'RoofCardV2style__BottomBarStyled-sc-xlmarl-3.eURsya')
        time.sleep(1)
        # print(l.text())
        l.click()
        time.sleep(5)

        try:


            badbath = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/p').text
        # print(badbath)
        except:
            pass


        split1 = badbath.split('|')
        split2 = split1[0].split(',')
        # print(split2)
        split3 = split2[0].split(' ')
        
        bedroom = split3[0]

        Beds_1.append(bedroom)

        print("bedroom",bedroom)
        split4 = split2[1].split(' ')
        # print("print", split2[1].split(' '))

        bathroom = split4[1]
        print("bathroom",bathroom)

        Baths_1.append(bathroom)


        Address = driver.find_element(By.CLASS_NAME,'MuiTypography-root.MuiTypography-body1.ListingHeaderstyle__AddressStreet-sc-1h7il48-7.lhrpgz.css-192l2bt')
        # time.sleep(3)
        Address_1.append(Address.text)
        print(Address.text)

        # Address_ = driver.find_element(By.CLASS_NAME,'MuiTypography-root.MuiTypography-subtitle1.ListingHeaderstyle__AddressCityStateZip-sc-1h7il48-8.SycFV.css-1wjdxzz')
        # # time.sleep(1)
        # Address_2.append(Address_.text)
        # print("===============")
        # print(Address_1)

        # print(Address_.text)



        price = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/span')
        # time.sleep(1)
        Price_1.append(price.text)
        # print(price.text)

        driver.execute_script('scrollTo(0,500)')
        time.sleep(2)

        try:

            tax = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div/div[3]/span')
            print('taxes => ',tax.text)
            Property_taxes_1.append(tax.text)

        except:
            Property_taxes_1.append("No Data")

        CLICK = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[3]/div/header/div/div[2]/div/button[2]')
        CLICK.click()
        time.sleep(3)
        # print('click_process_1 >>>>>')
    
        cash = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[3]/div/div[3]/div[1]/div/div/button[2]')
        cash.click()

        # time.sleep(1)
    

        try:
            rent = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[1]/div/div/div[5]/div[4]/div/div[2]/div/span')
            Monthly_Rent_1.append(rent.text)
            print(rent.text)
            time.sleep(1)
        except:
            Monthly_Rent_1.append("No Data")
        
        n = n+1
        print("Number of divs =>",n)

        driver.back()
        time.sleep(4)
        driver.back()
        time.sleep(4)


    # driver.find_element(By.CLASS_NAME,'svg-inline--fa.fa-chevron-right.fa-sm ').click()

    # time.sleep(5)


Dic = {
    'Address':Address_1,
    'Price':Price_1,
    'Monthly_Rent':Monthly_Rent_1,
    'Property_taxes':Property_taxes_1,
    'Beds':Beds_1,
    'Baths':Baths_1,
}

df = pd.DataFrame(Dic)
print(df)
     

       






