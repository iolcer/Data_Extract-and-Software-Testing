from selenium import webdriver
import loginInfo
import time

browser = webdriver.Chrome()
browser.get("https://twitter.com/twitter?lang=tr")
time.sleep(3)

giris_yap = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/header/div[2]/div[1]/div/div[2]/div[1]/div[1]/a/div/span/span")
                                           
giris_yap.click()

time.sleep(5)

username = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")

password = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

time.sleep(3)

login = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[3]/div/div")
                                       
login.click()

time.sleep(3)

searchArea = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
        

searchArea.send_keys("#yazilimayolver")

searchArea.submit()

time.sleep(3)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False

while(match==False):
    lastCount = lenOfPage
    time.sleep(3)

    elements = browser.find_elements_by_css_selector(".css-1dbjc4n.r-1iusvr4.r-18u37iz.r-16y2uox.r-1h0z5md")

    for element in elements:
        element.click()
        time.sleep(3)
 
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

time.sleep(5)
browser.close()

