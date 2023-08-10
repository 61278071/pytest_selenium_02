
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

class LoginPage:
    username_textbox_id="Email"
    password_textbox_id="Password"
    click_login_xpath="//button[@type='submit']"
    click_logout_xpath="//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self, driver):
        self.driver = driver


    def set_username(self,username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID,self.username_textbox_id).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.ID,self.password_textbox_id).clear()
        self.driver.find_element(By.ID,self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.click_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.click_logout_xpath).click()