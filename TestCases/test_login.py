
from POM.login_page import LoginPage
from UTILITIES.readProperties import ReadConfig
from UTILITIES.customLogger import LogGen


class Test_login:
    url = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homepage(self, setup):
        self.logger.info("****** Home Page Test started **********")
        self.driver = setup
        self.driver.get(self.url)
        title = self.driver.title
        if title == "Your store. Login":
            self.logger.info("****** Home Page Tested Successfully **********")
            assert True
        else:
            self.driver.save_screenshot("S:\\pycharm_practice_projects\\pytest_selenium_02\\Screenshots\\" + 'HomePageTestError.png')
            self.logger.error("****** Home Page Test Failed **********")
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        LP = LoginPage(self.driver)
        LP.set_username(self.username)
        LP.set_password(self.password)
        LP.click_login()
        title = self.driver.title
        if title == 'Dashboard / nopCommerce administration':
            self.logger.info("****** Login Test Passed **********")
            assert True
        else:
            self.driver.save_screenshot("S:\\pycharm_practice_projects\\pytest_selenium_02\\Screenshots\\" + 'LoginPageTestError.png')
            self.logger.error("****** Login Test Failed **********")
            assert False

