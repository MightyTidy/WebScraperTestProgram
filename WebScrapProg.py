import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def main():
    browser = webdriver.Chrome()
    browser.get("https://mail.google.com/mail/u/1/?tab=wm&ogbl#inbox")
    emailLogin = browser.find_element_by_id("identifierId")
    emailLogin.send_keys("mightytidy9@gmail.com")
    nextbutton = browser.find_element_by_id("identifierNext")
    nextbutton.click()
    browser.implicitly_wait(3)
    browser.find_element_by_css_selector("input[type=password").sendkeys("Jarjar99")
    passNext = browser.find_element_by_id('passwordNext')
    browser.execute_script("arguments[0].click();", passNext)
    writeEmailButton = browser.find_element_by_id(":ix")
    writeEmailButton.click()
    wait = WebDriverWait(browser, 5)
    addressBox = browser.find_element_by_id(":nu")
    addressBox.send_keys("mightytidy9@gmail.com")
    subjectBox = browser.find_element_by_id(":10q")
    subjectBox.send_keys("Test Email Webscraper Email")
    message = browser.find_element_by_id(":of")
    message.send_keys("This is my final message, goodbye")
    sendButton = browser.find_element_by_id(":s4")
    sendButton.click()


main()
