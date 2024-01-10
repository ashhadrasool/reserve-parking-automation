from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time

url = 'https://reservenski.parkpalisadestahoe-village.com/'
webdriver_path = '/Applications/Chromium.app/Contents/MacOS/Chromium'
username = 'abc'
password = '123'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)

try:
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

    time.sleep(5)
    driver.get('https://reservenski.parkpalisadestahoe-village.com/select-parking')

    current_date = datetime.now()

    days_until_saturday = (5 - current_date.weekday() + 7) % 7
    date_on_saturday = current_date.date() + timedelta(days=days_until_saturday)

    days_until_sunday = days_until_saturday + 1
    date_on_sunday = current_date.date() + timedelta(days=days_until_sunday)

    # print('date_on_saturday', date_on_saturday)

    calendar_selector = "//div[@role='grid'][@class='mbsc-calendar-table mbsc-calendar-table-active']"
    WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, calendar_selector)))

    if current_date.month != date_on_saturday.month:
        nextMonthButton = driver.find_element(By.XPATH, "//button[@class='mbsc-calendar-button mbsc-calendar-button-next mbsc-reset mbsc-font mbsc-button mbsc-ios mbsc-ltr mbsc-button-flat mbsc-icon-button']")
        nextMonthButton.click()
        time.sleep(5)

    calendar_element = driver.find_element(By.XPATH, calendar_selector)
    rows = calendar_element.find_elements(By.XPATH, ".//div[@role='row'][@class='mbsc-calendar-row']")
    days = calendar_element.find_elements(By.XPATH, ".//div[@class='mbsc-calendar-cell-text mbsc-calendar-day-text mbsc-ios']")

    for day in days:
        if day.text == str(date_on_saturday.day):
            day.click()
            time.sleep(5)
            break

    free_parking_on_saturday = False
    free_parking_on_sunday = False

    reservations_present = False
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="RatesPanel_emptyRatesHeadline__QNAAY"]')))
    except:
        reservations_present = True

    if reservations_present == True:
        parking_option_element_selector = '//div[@class="RatesPanel_ratesWrapper__1peNP"]'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, parking_option_element_selector)))
        parking_option_div_element = driver.find_element(By.XPATH, parking_option_element_selector)

        parking_options_selector = '//div[@class="RatesPanel_rateCopy__YOyL0"]'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, parking_options_selector)))
        parking_options = parking_option_div_element.find_elements(By.XPATH, parking_options_selector)

        for option in parking_options:
            if option.text.startswith('Free Reservation'):
                free_parking_on_saturday = True
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(2)
                option.click()
                park_for_free_selector = "//div[@class='ui basic center aligned segment']"
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, park_for_free_selector)))
                driver.find_element(By.XPATH, park_for_free_selector).click()
                time.sleep(2)
                confirm_button_selector = '//button[@class="ui button fluid PurchaseConfirm--button"]'
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, confirm_button_selector)))
                confirm_button = driver.find_element(By.XPATH, confirm_button_selector)
                confirm_button.click()
                time.sleep(10)
                break

    if(free_parking_on_saturday == True):
        print("Saturday - ", date_on_saturday, ": Free Parking Reserved ")
    else:
        print("Saturday - ", date_on_saturday, ": No Free Parking Available")

    driver.get('https://reservenski.parkpalisadestahoe-village.com/select-parking')
    WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, calendar_selector)))

    if current_date.month != date_on_sunday.month:
        nextMonthButton = driver.find_element(By.XPATH, "//button[@class='mbsc-calendar-button mbsc-calendar-button-next mbsc-reset mbsc-font mbsc-button mbsc-ios mbsc-ltr mbsc-button-flat mbsc-icon-button']")
        nextMonthButton.click()

        time.sleep(5)

    calendar_element = driver.find_element(By.XPATH, calendar_selector)
    rows = calendar_element.find_elements(By.XPATH, ".//div[@role='row'][@class='mbsc-calendar-row']")
    days = calendar_element.find_elements(By.XPATH, ".//div[@class='mbsc-calendar-cell-text mbsc-calendar-day-text mbsc-ios']")

    for day in days:
        if day.text == str(date_on_sunday.day):
            day.click()
            time.sleep(5)
            break

    reservations_present = False

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="RatesPanel_emptyRatesHeadline__QNAAY"]')))
    except:
        reservations_present = True

    if reservations_present == True:
        parking_option_element_selector = '//div[@class="RatesPanel_ratesWrapper__1peNP"]'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, parking_option_element_selector)))
        parking_option_div_element = driver.find_element(By.XPATH, parking_option_element_selector)

        parking_options_selector = '//div[@class="RatesPanel_rateCopy__YOyL0"]'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, parking_options_selector)))
        parking_options = parking_option_div_element.find_elements(By.XPATH, parking_options_selector)

        for option in parking_options:
            if option.text.startswith('Free Reservation'):
                free_parking_on_sunday = True
                driver.execute_script("window.scrollTo(0, 1500)")
                # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(2)
                option.click()
                park_for_free_selector = "//div[@class='ui basic center aligned segment']"
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, park_for_free_selector)))
                driver.find_element(By.XPATH, park_for_free_selector).click()
                time.sleep(2)
                confirm_button_selector = '//button[@class="ui button fluid PurchaseConfirm--button"]'
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, confirm_button_selector)))
                confirm_button = driver.find_element(By.XPATH, confirm_button_selector)
                confirm_button.click()
                time.sleep(10)
                break

    if(free_parking_on_sunday == True):
        print("Sunday   - ", date_on_sunday, ": Free Parking Reserved")
    else:
        print("Sunday   - ", date_on_sunday, ": No Free Parking Available")

except Exception as e:
    raise e
finally:
    driver.quit()
