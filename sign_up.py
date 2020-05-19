"""
The program navigates all of the pages that are required to get to the
add CRN page in Foothill's system. The code successfully enrolls the
user into their desired CRN. The current iteration of the program only
allows for one CRN to be added.
"""

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


def login():
    """Completes the login process for the user."""
    driver.get('https://myportal.fhda.edu/')
    user_name = '' #enter your username
    password = '' #enter your password
    username_path = '//*[@id="j_username"]'
    password_path = '//*[@id="j_password"]'
    submit_button = '//*[@id="btn-eventId-proceed"]'
    driver.find_element_by_xpath(username_path).send_keys(user_name)
    time.sleep(1)
    driver.find_element_by_xpath(password_path).send_keys(password)
    driver.find_element_by_xpath(submit_button).click()


def registration_page():
    """Navigates the app and moves onto the add/drop page"""
    app_button = '//*[@id="react-portal-root"]/div/div[1]/div[1]/ul/li[3]'
    student_registration = '//*[@id="react-portal-root"]/div/div[1]/div[2]' \
                           '/div[2]/div/div[2]/div/div'
    add_drop_button = '//*[@id="react-portal-root"]/div/div[1]' \
                      '/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[3]/a'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, app_button)))
    time.sleep(1)
    driver.find_element_by_xpath(app_button).click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(.1)
    driver.find_element_by_xpath(student_registration).click()
    time.sleep(.1)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, add_drop_button)))
    driver.find_element_by_xpath(add_drop_button).click()


def term_selection():
    """Selects the term of interest"""
    submit_button = '/html/body/div[3]/form/input'
    select = Select(driver.find_element_by_id('term_id'))
    select.select_by_index('')  #insert the term of interest
    driver.find_element_by_xpath(submit_button).click()


def enter_crn():
    """Enters the CRN that you want to be enrolled in and submits it"""
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    crn = ''  #enter the crn you would like to enroll in
    first_crn_box = '//*[@id="crn_id1"]'
    driver.find_element_by_xpath(first_crn_box).send_keys(crn)
    driver.find_element_by_xpath(first_crn_box).send_keys(u'u\ue007')


def main():
    """Initiates all of the functions with the needed pauses to ensure
    completion"""
    login()
    registration_page()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.window(driver.window_handles[0])
    term_selection()
    time.sleep(2)
    enter_crn()
    print("Done")


if __name__ == '__main__':
    driver = webdriver.Safari()
    main()