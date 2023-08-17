#from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import time

# Replace with your friend's Twitter username
friend_username = 'sierpc69'

# Path to your browser driver (e.g., chromedriver for Chrome)
browser_driver_path = 'geckodriver'

# Create a new instance of the Chrome browser
browser = webdriver.Firefox()

# Open Twitter and log in
browser.get('https://twitter.com/')
time.sleep(20)  # Let the page load
# Add code to log in if needed

# Visit your friend's profile
browser.get(f'https://twitter.com/{friend_username}')
time.sleep(3)  # Let the page load
count = 0
while count == 0:
    # Visit your friend's profile
    browser.get(f'https://twitter.com/{friend_username}')
    time.sleep(3)  # Let the page load

    # Follow your friend
    follow_button = browser.find_element(By.CSS_SELECTOR, 'div[data-testid="placementTracking"]')
    follow_button.click()

    # Wait for a while
    time.sleep(3)

    # Unfollow your friend
    unfollow_button = browser.find_element(By.CSS_SELECTOR, 'div[data-testid="placementTracking"]')
    unfollow_button.click()
    unfollow_confirm = browser.find_element(By.CSS_SELECTOR, 'div[data-testid="confirmationSheetConfirm"]')
    unfollow_confirm.click()

    # Wait for a while before the next iteration
    time.sleep(3)
