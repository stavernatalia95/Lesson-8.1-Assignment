from selenium import webdriver
from selenium.webdriver.support.color import Color

#imports for selenium WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='Drivers/chromedriver.exe')
driver.get("https://techskillacademy.net/brainbucket/index.php?route=account/login")

driver.maximize_window()  #m aximizing the browser window

logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

# Natalia 5/6/21
# when you are clicking on the "Continue" or "Login" buttons,
# use WebDriverWait with expected condition element_to_be_clickable instead of driver.find_element_by*

wait=WebDriverWait(driver, 10)
new_registrant_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Continue')]")))


#getting the background color of the button
backround_color = new_registrant_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(backround_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
new_registrant_btn.click()

# Natalia 5/6/21
# after clicking on the “Continue” button Registration page should launch.
# Add an explicit wait here until the “Register Account” title will be visible.

register_account=wait.until(
    EC.visibility_of_element_located((By.XPATH, "//h1[contains(.,'Register Account')]")))

#Register Account
#Personal Details
firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Natalia")

# Natalia Staver 4/25/2021


# Last Name Input
lastname_field = driver.find_element_by_xpath("//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.clear()
lastname_input.send_keys("Staver")

# e-mail input
e_mail_field = driver.find_element_by_xpath("//fieldset/div[4]")
e_mail_field_class = e_mail_field.get_attribute("class")
assert "required" in e_mail_field_class

e_mail_input = driver.find_element_by_id("input-email")
e_mail_input.clear()
e_mail_input.send_keys("staver.natalia@yahoo.com")

# Telephone
telephone_field = driver.find_element_by_xpath("//fieldset/div[5]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class

telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.clear()
telephone_input.send_keys("589-663-0000")

# Verifies background-color of Continue button

continue_botton = driver.find_element_by_xpath("//input[@class='btn btn-primary']")

backround_color = continue_botton.value_of_css_property("background-color")
converted_background_color = Color.from_string(backround_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
continue_botton.click()

# Locates the password field on the Login Page, enters the password, and then click the “Login” button.

driver.get("https://techskillacademy.net/brainbucket/index.php?route=account/login")
returning_customer_password=driver.find_element_by_xpath("//input[@id='input-password']")

returning_customer_password_input = driver.find_element_by_id("input-password")
returning_customer_password_input.clear()
returning_customer_password.send_keys("2100Golf!")

returning_customer_login_btn=driver.find_element_by_xpath('//input[@value="Login"]')
returning_customer_login_btn.click()
