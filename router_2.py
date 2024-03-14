from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

def reboot(website):
    # Webdriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    browser = webdriver.Chrome(options=chrome_options)

    print("Initialized chrome headless")

    # Goto tenda router webpage
    browser.get(website)

    print("Opened router website")

    # Wait for system button to load
    button_system = WDW(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'system'))
    )

    # Click system button
    browser.execute_script("arguments[0].click()", button_system)

    # Wait for reboot button to load
    button_reboot = WDW(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'reboot'))
    )

    # Click reboot button
    browser.execute_script("arguments[0].click()", button_reboot)

    # Switch to alert and accept it
    browser.switch_to.alert.accept()

    print("Reboot initialized successfully")