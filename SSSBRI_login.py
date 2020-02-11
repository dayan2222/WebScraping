from selenium import webdriver

with open('student_details.csv' , 'w') as f:
    f.write("S.No , Student Name, Student ID \n")

driver = webdriver.Chrome()


driver.get('http://dayanahmed66.pythonanywhere.com/dashboard')

user_name = driver.find_element_by_xpath('//*[@id="uname"]')
user_name.send_keys('admin')

driver.implicitly_wait(4)

password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('password')

driver.implicitly_wait(4)


login = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/form/button')
login.click()

driver.implicitly_wait(10)

students_list = driver.find_element_by_xpath('//*[@id="accordionSidebar"]/li[4]/a/span')
students_list.click()

driver.implicitly_wait(10)

for i in range(1,5):

    # TODO:Fetch the Data from table

    sno = driver.find_element_by_xpath('//*[@id="dataTable"]/tbody/tr['+str(i)+']/td[1]')
    student_name = driver.find_element_by_xpath('//*[@id="dataTable"]/tbody/tr[' + str(i) + ']/td[2]')
    student_id = driver.find_element_by_xpath('//*[@id="dataTable"]/tbody/tr[' + str(i) + ']/td[3]')

    with open('student_details.csv', 'a') as f:
        f.write(sno.text + ',' + student_name.text + ',' + student_id.text + '\n')
    print(sno.text)
    print(student_name.text)
    print(student_id.text)


driver.close()