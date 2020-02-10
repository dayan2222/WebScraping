from selenium import webdriver
# executable_path='C:\\Users\\Dayan Ahmed\\Desktop\\Web Scrapping\\chromedriver_win32\\chromedriver.exe'
#path = 'chromedriver'
driver = webdriver.Chrome(executable_path='C:\\Users\\Dayan Ahmed\\Desktop\\Web Scrapping\\chromedriver_win32\\chromedriver')


driver.get('https://gmail.com/')

user_name = driver.find_element_by_xpath('//*[@id="identifierId"]')
user_name.send_keys('your_mail@gmail.com')

driver.implicitly_wait(4)

button_next = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
button_next.click()


driver.implicitly_wait(4)

password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys('password')


driver.implicitly_wait(4)

login = driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
login.click()



driver.close()