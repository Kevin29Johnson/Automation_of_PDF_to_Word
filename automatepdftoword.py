from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
fp=input(r"Enter full file path:") # enter pdf file path
print()
fn=input("Enter file name:")
fo=fp+fn+".pdf"
time.sleep(10)
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.ilovepdf.com/pdf_to_word")
time.sleep(10)
file=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/input")
file.send_keys(fo)
time.sleep(10)
driver.find_element_by_xpath("//*[@id='processTask']").click()#Convert button
time.sleep(10)
driver.find_element_by_xpath("//*[@id='pickfiles']").click()#Download button
time.sleep(1)
driver.quit()

