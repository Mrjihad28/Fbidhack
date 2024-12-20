from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the Selenium webdriver
driver = webdriver.Chrome()

# Navigate to the Facebook login page
driver.get("https://www.facebook.com/")

# Find the email and password input fields and enter your credentials
email_input = driver.find_element_by_id("email")
password_input = driver.find_element_by_id("pass")
email_input.send_keys("YOUR_FACEBOOK_EMAIL")
password_input.send_keys("YOUR_FACEBOOK_PASSWORD")

# Submit the login form
password_input.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(5)

# Navigate to the target profile page
driver.get("https://www.facebook.com/TARGET_PROFILE_ID")

# Wait for the page to load
time.sleep(5)

# Find the "Follow" button and click it
follow_button = driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
follow_button.click()

# Wait for the page to load
time.sleep(5)

# Find the "Like" button and click it
like_button = driver.find_element_by_xpath("//span[contains(text(), 'Like')]")
like_button.click()

# Wait for the page to load
time.sleep(5)

# Close the browser
driver.quit()
