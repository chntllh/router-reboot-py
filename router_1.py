from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

def reboot(website, username, password):
    # Webdriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    browser = webdriver.Chrome(options=chrome_options)

    print("Initialized chrome headless")

    # Goto main router website
    browser.get(website)

    print("Opened router website")

    # Wait for username text box to load and enter username
    WDW(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    ).send_keys(username)

    # Wait for password text box to load and enter password
    WDW(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'psd'))
    ).send_keys(password)

    # Find value of verification
    value_verification = browser.find_element(By.ID, 'check_code').get_attribute('value')

    # Wait for verification code text box to load and enter password
    WDW(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'verification_code'))
    ).send_keys(value_verification)

    # Click login button
    browser.find_element(By.XPATH, "//input[@value='Login']").click()

    print("Login success")

    # Wait for 'topFrame' to load and switch to it
    WDW(browser, 10).until(
        EC.frame_to_be_available_and_switch_to_it('topFrame')
    )

    # Naviagtion button
    browser.find_element(By.XPATH, '/html/body/form/table[2]/tbody/tr[2]/td/table/tbody/tr/td[5]/p/b/font/a/span').click()

    # Nagivation button
    browser.find_element(By.XPATH, '/html/body/form/table[2]/tbody/tr[3]/td/table/tbody/tr/td[3]/p/a/span').click()

    # Switch to default frame
    browser.switch_to.default_content()

    # Swtich to 'mainFrame'
    browser.switch_to.frame('mainFrame')

    # Wait for reboot button to load
    button_reboot = WDW(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/blockquote/div/form/p/input[1]'))
    )

    # Click reboot button
    browser.execute_script("arguments[0].click();", button_reboot)

    print("Reboot initialized successfully")