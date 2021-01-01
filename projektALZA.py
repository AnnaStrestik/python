from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.alza.cz/evga-geforce-rtx-2060-super-sc-ultra-gaming-d5677268.htm')

checkbox = driver.find_element_by_id("hlOrderFast").click() 

# checkbox.click()
# submit = driver.find_element_by_id('submit')
# submit.click()


# quantity_text = driver.find_element_by_id('product_62')
# quantity_text.send_keys('1')

# fields = {'name': 'Alex Recker',
#           'Address': '123 Sesame St',
#           'City': 'Madison',
#           'Zip': '53704',
#           'email': 'alex@reckerfamily.com'}
# for name, value in fields.items():
#     elem = driver.find_element_by_name(name)
#     elem.send_keys(value)


#     else:
#         elem = driver.find_element_by_name(name)
#         elem.send_keys(value)
# driver.find_element_by_name('notice').click()  # same as billing address...
# driver.find_element_by_id('submit').click()