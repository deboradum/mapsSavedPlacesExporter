# Opens every saved place from a google exported JSON/ CSV file of your Google
# Maps places to make transferring across accounts easy.


import json
import time

# Webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# Initialises driver.
try:
    # Detection avoidance options.
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')

    # Chromedriver location
    ser = Service("/usr/local/bin/chromedriver")

    driver = webdriver.Chrome(options=options, service=ser)
except Exception as e:
    print(e)


# Path of the csv or json file to be used.
filePath = "saved/Favorite places.csv"
file = open(filePath)

# Goes to log in page for google. User needs to be logged in to save maps to
# account.
driver.get("https://accounts.google.com/signin")
input("Press Enter when logged in.")


# For JSON files.
data = json.load(file)
data = data["features"]
count = 0
for el in data:
    try:
        link = el["properties"]["Google Maps URL"]
        driver.get(link)
        input("Press Enter to continue.")

        # Finds buttons to add.
        save_btn = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[2]/button")
        save_btn.click()
        time.sleep(1) # Wait until loaded.
        overnacht_btn = driver.find_element(by=By.XPATH, value="//div[contains(text(), 'starred')]/parent::div/parent::li")
        overnacht_btn.click()
        time.sleep(2.5) # Wait until added.
    except Exception as e:
        print(e)
        print("error at: " + link + " continuing.\n")
