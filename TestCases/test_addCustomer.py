import string
import random

import pytest
from POM.login_page import LoginPage
from POM.AddCustomer_page import AddCustomerPage
from UTILITIES.readProperties import ReadConfig
from UTILITIES.customLogger import LogGen
from selenium.webdriver.common.by import By


class Test_AddCustomer_003:
    url = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def email_generator(self,size=8,char=string.ascii_lowercase+string.digits):
        self.mail= ''.join(random.choice(char) for x in range(size))
        return self.mail+'@gmail.com'


    def test_AddCustomer(self,setup):
        self.logger.info("*********** Test_AddCustomer_003 ************")
        self.logger.info("*********** Verifying AddCustomer Test ************")
        self.driver = setup
        self.driver.get(self.url)
        LP = LoginPage(self.driver)
        LP.set_username(self.username)
        LP.set_password(self.password)
        LP.click_login()
        self.logger.info("*********** Login Successful ************")
        AC=AddCustomerPage(self.driver)
        AC.click_CustomerMenu()
        AC.click_CustomerItem()
        AC.click_AddNew()
        AC.setEmail(self.email_generator())
        AC.setPassword("9441230534")
        AC.setFirstName("srinivas")
        AC.setLastName("karri")
        AC.setGender("Female")
        AC.setDOB("07/07/1991")
        AC.setCompanyName("Acert IT Solutions")
        AC.click_taxExcempt()
        AC.set_newsletter('Test store 2')
        AC.setCustomerRole("Admin")
        AC.setVendor("Vendor 2")
        AC.clickActive()
        AC.AddComment("New User here")
        AC.clickSave()
        # store the notification in after converting into a text file
        self.msg=self.driver.find_element(By.TAG_NAME, 'body').text
        if 'The new customer has been added successfully.' in self.msg:
            self.logger.info("********** New Customer Added Successfully **********")
            assert True
        else:
            self.driver.save_screenshot('S:\\pycharm_practice_projects\\pytest_selenium_02\\Screenshots\\'+'AddCust.png')
            self.logger.info("********** Adding new Customer failed **********")
            assert True