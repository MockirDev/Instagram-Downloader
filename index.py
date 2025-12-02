from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
import yt_dlp

browser = webdriver.Chrome()

browser.get('https://www.instagram.com/')

time.sleep(5)

#Giriş
browser.find_element(By.NAME, 'username').send_keys("yourusername")
browser.find_element(By.NAME, 'password').send_keys("yourpassword")

time.sleep(2)
browser.find_element(By.CLASS_NAME, 'qF0y9.Igw0E.IwRSH.eGOV_.acqo5_4EzTm').click()
browser.find_element(By.XPATH, "//button[class()='sqdOP.L3NKy.y3zKF.']").click()
time.sleep(3)
#Hesapların Son Gönderilerini alma
try:
  browser.get('https://www.instagram.com/username/') 
  time.sleep(3)
  browser.find_element(By.CLASS_NAME, 'div..qF0y9.Igw0E.rBNOH.eGOV_.ybXk5._4EzTm').click()
  time.sleep(5)
  browser.find_element(By.CLASS_NAME, 'JB3Yj').click()
  time.sleep(3)
  browser.find_element(By.CLASS_NAME, 'MEAGs ').click()
  time.sleep(3)
  button2 = browser.find_element(By.XPATH, "//button[text()='Bağlantıyı Kopyala']")
  browser.execute_script("arguments[0].click();", button2)
except:
    print(e)  
finally:
  try:
    ydl_opts = {'writesubtitles': True, 'skip-download': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([pyperclip.paste])
  except:
    print('İndirme sırasında bir sorun oluştu.')

