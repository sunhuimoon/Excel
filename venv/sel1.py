from time import sleep
from selenium import webdriver

chrome = webdriver.Chrome()
chrome.get("http://xue.ujiuye.com/foreuser/login/")
username_d1 = chrome.find_element_by_id("username_dl")
password_dl = chrome.find_element_by_id("password_dl")
button = chrome.find_elements_by_class_name("loginbutton1")
username_d1.send_keys("13331153361")
password_dl.send_keys("1234556")
button[0].click()
sleep(2)
#text = self.chrome.find_element_by_id("J_usernameTip").text
text = chrome.find_element_by_id("J_usernameTip").text
print (text)
#J_usernameTip     //*[@id="J_usernameTip"]
#text="账号不存在"