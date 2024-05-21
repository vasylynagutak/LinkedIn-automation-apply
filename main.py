from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os

load_dotenv()

chrome_driver_path ="/Applications"
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3610503826&f_AL=true&f_E=2%2C3&geoId=90009551&keywords=qa%20engineer&location=Greater%20Toronto%20Area%2C%20Canada&refresh=true")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
PHONE = os.getenv("PHONE")
print(f"Email: {MY_EMAIL}, Password: {MY_PASSWORD}, Phone: {PHONE}")

sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

#Wait for the next page to load.
time.sleep(2)

email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(MY_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(MY_PASSWORD)
password_field.send_keys(Keys.ENTER)



all_listings = driver.find_element(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(3)
while True:
    try:
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        phone = driver.find_element(by=By.CLASS_NAME, value="fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        submit_button.click()
        time.sleep(2)

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(by=By.CLASS_NAME,value="artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
            print("No application button, skipped.")
            continue

    time.sleep(5)
    driver.quit()


