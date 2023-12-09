from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time


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

    calendar_selector = "//div[@role='grid'][@class='mbsc-calendar-table mbsc-calendar-table-active']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, calendar_selector)))
    calendar_element = driver.find_element(By.XPATH, calendar_selector)
    rows = calendar_element.find_elements(By.XPATH, ".//div[@role='row'][@class='mbsc-calendar-row']")

    current_date = datetime.now()

    days_until_saturday = (5 - current_date.weekday() + 7) % 7
    date_on_saturday = current_date.date() + timedelta(days=days_until_saturday)

    print(current_date.day)
    print(current_date.date())
    print('date_on_saturday', date_on_saturday)

    if current_date.month == date_on_saturday.month:
        days = calendar_element.find_elements(By.XPATH, ".//div[@class='mbsc-calendar-cell-text mbsc-calendar-day-text mbsc-ios']")
        for day in days:
            print(day.text)
            if day.text == str(date_on_saturday.day):
                day.click()
                break

        parking_option_element_selector = '//div[@class="RatesPanel_ratesWrapper__1peNP"]'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, parking_option_element_selector)))
        parking_option_div_element = driver.find_element(By.XPATH, parking_option_element_selector)

        parking_options_selector = '//div[@class="RatesPanel_rateCopy__YOyL0"]'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, parking_options_selector)))
        parking_options = parking_option_div_element.find_elements(By.XPATH, parking_options_selector)


        for option in parking_options:
            if option.text == 'Advanced Paid Reservations':
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(2)
                option.click()
                break


    time.sleep(2)
    login_button_selector = '//a[@href="/login"]'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_button_selector)))
    login_button = driver.find_element(By.XPATH, login_button_selector)
    login_button.click()

    username_field = driver.find_element(By.ID, 'emailAddress')
    password_field = driver.find_element(By.ID, 'password')

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
    login_button.click()

    print()

finally:
    driver.quit()
