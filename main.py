from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
import time
import pprint
from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "html.parser")
cards_data = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

links_list = [card.find("a").get("href") for card in cards_data]
prices_list = [card.find("span", class_="PropertyCardWrapper__StyledPriceLine").text.split("+")[0].strip("/mo") for card in cards_data]
addresses_list = [card.find("address").text.strip() for card in cards_data]

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdjERY-mW1Omu9dz5DSw_e1oc9v2rdCRmnZub92hLJuRIxxxw/viewform")
time.sleep(3)

for i in range(len(links_list)):
    form_inputs = driver.find_elements(By.CSS_SELECTOR, value="input[jsname='YPqjbf']")
    form_inputs[0].click()
    time.sleep(3)
    form_inputs[0].send_keys(addresses_list[i])
    form_inputs[1].click()
    time.sleep(3)
    form_inputs[1].send_keys(prices_list[i])
    form_inputs[2].click()
    time.sleep(3)
    form_inputs[2].send_keys(links_list[i])
    time.sleep(3)
    submit = driver.find_element(By.XPATH, value="//span[text()='إرسال']")
    submit.click()
    time.sleep(3)
    send_another_response = driver.find_element(By.XPATH, value="//a[text()='إرسال رد آخر']")
    send_another_response.click()
    time.sleep(7)
