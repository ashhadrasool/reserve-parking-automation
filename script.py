from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://reservenski.parkpalisadestahoe-village.com/'
webdriver_path = '/Applications/Chromium.app/Contents/MacOS/Chromium'
username = 'katz.tavi123@gmail.com'
password = 'PalisadesParking'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(options=chrome_options)

driver.get(url)

try:
    select_parking_link = driver.find_element(By.XPATH, "//a[@href='/select-parking']")

    select_parking_link.click()

    find_calendar = driver.find_element(By.XPATH, "//div[@class='mbsc-calendar-wrapper mbsc-ios']")

    find_calendar.click()



    # username_field = driver.find_element(By.ID, 'emailAddress')  # Replace with the actual ID of the username field
    # password_field = driver.find_element(By.ID, 'password')  # Replace with the actual ID of the password field
    #
    # username_field.send_keys(username)
    # password_field.send_keys(password)
    #
    # login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')  # Adjust the XPath as needed
    # login_button.click()

finally:
    # Close the browser window
    driver.quit()
