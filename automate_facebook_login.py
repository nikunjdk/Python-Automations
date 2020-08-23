#! python3
# Automate Facebook Login
from selenium import webdriver

# browser = webdriver.Edge(webdriver.exe path)
browser = webdriver.Edge('D:\\Programming\\Python\\webdriver\\msedgedriver.exe')

# browser.get(target website url)
browser.get('https://www.facebook.com/')

# You can take the input from the user or hardcode the value
user_id = input('Enter email id or phone number: ')
password = input('Enter password: ')

# element = browser.find_element_by_id(target object id)
email_field_id = browser.find_element_by_id('email')
pass_field_id = browser.find_element_by_id('pass')
login_button_id = browser.find_element_by_id('u_0_b')

# element.send_keys(object to be sent to targetted id)
email_field_id.send_keys(user_id)
pass_field_id.send_keys(password)

# element.click() - Click the targetted element
login_button_id.click()

# Close the browser
browser.quit()