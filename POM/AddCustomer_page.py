from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
class AddCustomerPage:

    Link_CustomerMenu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    Link_CustomerItem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btn_Addnew_xpath = "//a[@class='btn btn-primary']"
    txtBox_Email_xpath = "//*[@id='Email']"
    txtBox_Password_xpath = '//*[@id="Password"]'
    txtBox_FirstName_xpath = '//*[@id="FirstName"]'
    txtBox_LastName_xpath = '//*[@id="LastName"]'
    chBox_Male_xpath = '//*[@id="Gender_Male"]'
    chBox_Female_xpath = '//*[@id="Gender_Female"]'
    txtBox_dob_xpath = '//*[@id="DateOfBirth"]'
    txtBox_Company_xpath = '//*[@id="Company"]'
    chBox_IstaxExcempt_xpath = '//*[@id="IsTaxExempt"]'
    ListBox_NewsLetter_xpath = "//div/div[9]//div[@role='listbox']"
    ListBox_CustRoleAdm_xpath = "//li[text()='Administrators']"
    ListBox_CustRoleFM_xpath = "//li[text()='Forum Moderators']"
    ListBox_CustRoleGuests_xpath = "//li[text()='Guests']"
    ListBox_CustRoleRegd_xpath = "//li[text()='Registered']"
    ListBox_CustRoleVendors_xpath = "//li[text()='Vendors']"
    cancel_CurtRoleRegistered_xpath = '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]'
    drp_VendorID_xpath = "//select[@id='VendorId']"
    chBox_Active_xpath = "//input[@id='Active']"
    txtBox_AdminComment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver
    def click_CustomerMenu(self):
        self.customerMenu=self.driver.find_element(By.XPATH, self.Link_CustomerMenu_xpath)
        self.driver.execute_script('arguments[0].click();',self.customerMenu)
    def click_CustomerItem(self):
        self.customerItem=self.driver.find_element(By.XPATH, self.Link_CustomerItem_xpath)
        self.driver.execute_script('arguments[0].click();',self.customerItem)
    def click_AddNew(self):
        self.driver.find_element(By.XPATH, self.btn_Addnew_xpath).click()
    def setEmail(self,Email):
        self.driver.find_element(By.XPATH, self.txtBox_Email_xpath).send_keys(Email)
    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtBox_Password_xpath).send_keys(password)
    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH, self.txtBox_FirstName_xpath).send_keys(firstname)
    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH, self.txtBox_LastName_xpath).send_keys(lastname)
    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.chBox_Male_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.chBox_Female_xpath).click()
    def setDOB(self,dob):
        self.driver.find_element(By.XPATH, self.txtBox_dob_xpath).send_keys(dob)
    def setCompanyName(self,company):
        self.driver.find_element(By.XPATH, self.txtBox_Company_xpath).send_keys(company)
    def click_taxExcempt(self):
        self.driver.find_element(By.XPATH, self.chBox_IstaxExcempt_xpath).click()

    def set_newsletter(self,news):
        if news == 'default':
            self.LB_newsletter_xpath='//li[text()="Your store name"]'
        else:
            self.LB_newsletter_xpath='//li[text()="Test store 2"]'
        self.newsletter=self.driver.find_element(By.XPATH, self.LB_newsletter_xpath)
        self.driver.execute_script('arguments[0].click()',self.newsletter)
    def setCustomerRole(self,role):
        if role == "Guest":
            self.driver.find_element(By.XPATH, self.cancel_CurtRoleRegistered_xpath).click()#  remove Registered in LB
            self.guest=self.driver.find_element(By.XPATH, self.ListBox_CustRoleGuests_xpath)
            self.driver.execute_script("arguments[0].click()",self.guest)
        elif role == "Admin":
            self.Admin=self.driver.find_element(By.XPATH, self.ListBox_CustRoleAdm_xpath)
            self.driver.execute_script('arguments[0].click()',self.Admin)
        elif role == "Vendor":
            self.vendor=self.driver.find_element(By.XPATH, self.ListBox_CustRoleVendors_xpath)
            self.driver.execute_script('arguments[0].click()',self.vendor)
        else:
            pass

    def setVendor(self,vendor):
        # driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH,self.ListBox_CustRoleVendors_xpath))
        # driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, self.cancel_CurtRoleRegistered_xpath))
        select_vendor = Select(self.driver.find_element(By.XPATH, self.drp_VendorID_xpath))
        if vendor == 'vendor 1':
            select_vendor.select_by_visible_text('Vendor 1')
        elif vendor == 'vendor 2':
            select_vendor.select_by_visible_text('Vendor 2')


    def clickActive(self):
        self.driver.find_element(By.XPATH, self.chBox_Active_xpath).click()
    def AddComment(self,text):
        self.driver.find_element(By.XPATH, self.txtBox_AdminComment_xpath).send_keys(text)
        time.sleep(10)
    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
