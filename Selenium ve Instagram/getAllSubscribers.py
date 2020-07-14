from selenium import webdriver
import pyautogui
import time
import loginInfo

browser = webdriver.Chrome()
browser.get("https://www.instagram.com")
time.sleep(2)

#girisYap = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[2]/p/a")
#girisYap.click()

username = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
password = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

loginButton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]/button/div")

loginButton.click()
time.sleep(5)

pyautogui.click(756,23)

time.sleep(5)

pyautogui.click(833,633)

time.sleep(5)

pyautogui.click(839,703)

profil = browser.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a")
profil.click()
time.sleep(3)

followers = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
followers.click()
time.sleep(5)

jscommand = """
followers=document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;

"""
lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(5)
followersList = []

followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

for follower in followers:
    followersList.append(follower.text)

with open("followers.txt", "w", encoding = "UTF-8") as file:
    for follower in followersList:
        file.write(follower + "\n")
             


browser.close()
