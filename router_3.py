from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

def reboot(website, password):
    # Webdriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    browser = webdriver.Chrome(options=chrome_options)

    print("Initialized chrome headless")

    # Goto tp-link router website
    browser.get(website)

    print("Opened router website")

    # Wait for password-text box to load
    password_input = WDW(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'password-text'))
    )

    # Enter password in the password-text box
    password_input.send_keys(password)

    # Wait for login button to load
    login_button = WDW(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/a'))
    )

    # Click the login button
    browser.execute_script("arguments[0].click();", login_button)

    print("Login success")

    # Wait for System button in the top navigation bar to load
    nav_link1 = WDW(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[3]/div/div[1]/ul/li[4]/a/span[1]'))
    )

    # Click the System button
    browser.execute_script("arguments[0].click();", nav_link1)

    # Wait for Reboot button in the left navigation bar to load
    nav_link2 = WDW(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div[1]/ul/li[9]/a/span[2]'))
    )

    # Click reboot button in left navigation panel
    browser.execute_script("arguments[0].click();", nav_link2)

    # Wait for reboot button 
    reboot_button = WDW(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='button-button' and @title='REBOOT']"))
    )

    # Click the reboot button
    browser.execute_script("arguments[0].click();", reboot_button)

    # Wait for confirmation button to load
    confirm_button = WDW(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="reboot-confirm-msg-btn-ok"]'))
    )

    # Click the confirmation button
    browser.execute_script("arguments[0].click();", confirm_button)

    print("Reboot initialized successfully")