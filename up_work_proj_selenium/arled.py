from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

 
#above lines import dependent libraries
 
driver=webdriver.Chrome() #this line launches a chrome instance
 
driver.get('https://matrix.brightmls.com/Matrix/Public/Portal.aspx?ID=0-4160670010-10&eml=amFrZUBqc3F1YXJlZDJsbGMuY29t&rk=1346975474') #fetches passed url
 
shell = win32com.client.Dispatch("WScript.Shell") #win32com provides access to automation modules.
 
# shell.Sendkeys("username")  #SendKeys are used to send input to authentication alert boxes
 
time.sleep(2) #pauses execution for 2 seconds
 
 
shell.Sendkeys("{ENTER}")
time.sleep(2)
driver.quit()