from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import geckodriver_autoinstaller
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = Service("C:Users/User/chromedriver")
driver = webdriver.Chrome(service=chrome_driver_path,  chrome_options=chrome_options)

# -------------------------------------- Using firefox ---------------------------------------------------
# profile = webdriver.FirefoxProfile("C:/Users/User/AppData/Roaming/Mozilla/Firefox/Profiles/9d2htce0.default-release")
# profile.set_preference("dom.webdriver.enabled", False)
# profile.set_preference('useAutomationExtension', False)
# profile.update_preferences()
# desired = DesiredCapabilities.FIREFOX
#
# driver = webdriver.Firefox(firefox_profile=profile,
#                            desired_capabilities=desired)

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

response = requests.get("https://www.foodadvisor.my/best-cafes-kl")
content = response.text

soup = BeautifulSoup(content, "html.parser")

cafe_list = []
all_cafe = soup.select(selector=".link")
for cafe in all_cafe:
    cafe_list.append(cafe.getText())

print(cafe_list)

link_list = []
all_link = soup.select(selector=".link")
for link in all_link:
    link_list.append(link.get("href"))


address_list = []

all_address = soup.select(selector=".col-sm-9")
for address in all_address:
    address_only = address.select_one("span").getText()
    new_address = address_only[0:-19]
    address_list.append(new_address)
print(address_list)


for _ in range(len(cafe_list)):
    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLScC7U93vyQGIE4QMCBDY4-C5_3tBOJrsfoctA-TaLJx4pOpKQ/viewform?usp=sf_link")

    fill_cafe_name = driver.find_element(By.XPATH,
                                         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    fill_address = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill_cafe_link = driver.find_element(By.XPATH,
                                         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    fill_cafe_name.send_keys(cafe_list[_])
    fill_address.send_keys(address_list[_])
    fill_cafe_link.send_keys(link_list[_])
    submit_form = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_form.click()

driver.get("https://docs.google.com/forms/d/1EZrXIM8MFDkFefC4BtsHXfkk529-zUCP-zukFk07Bgw/edit#responses")
excel_button = driver.find_element(By.XPATH,'//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span')
excel_button.click()
create_button = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[61]/div/div[2]/div[2]/div[3]/div[1]/span/span')
create_button.click()
