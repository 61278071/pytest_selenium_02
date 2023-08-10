import pytest
from POM.login_page import LoginPage
from UTILITIES.readProperties import ReadConfig
from UTILITIES.customLogger import LogGen
from UTILITIES import XLUtils

class Test_login_ddt:
    url = ReadConfig.getURL()
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("************ TEST_LOGIN_DDT *******")
        self.logger.info("************ VERIFYING LOGIN_DDT TEST *******")
        self.driver = setup
        self.driver.get(self.url)
        self.LP = LoginPage(self.driver)
        path="S:\\pycharm_practice_projects\\pytest_selenium_02\\TESTDATA\\LoginData.xlsx"
        rows=XLUtils.getRowCount(path,'Sheet1')

        test_status=[]
        for r in range(2,rows+1):
            self.username = XLUtils.readData(path,'Sheet1',r,1)
            self.password = XLUtils.readData(path,'Sheet1',r,2)
            self.exp=XLUtils.readData(path,'Sheet1',r,3)
            self.LP.set_username(self.username)
            self.LP.set_password(self.password)
            self.LP.click_login()
            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'
            '''
            username password exp               login          test
            valid     valid   pass--------------success/pass   Passed
            Invalid  Invalid  Fail              success/pass   Failed
            Invalid  Invalid  Fail              Failed         Passed
            Valid     Valid   pass              Failed         Failed'''
            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**********Login successful_ValidData***Test-Passed********")
                    self.LP.click_logout()
                    self.logger.info("********** Logged Out successful **********")
                    test_status.append('Pass')
                elif self.exp == 'Fail':
                    self.logger.info("**********Login successful_InValidData***Test-Failed********")
                    self.LP.click_logout()
                    test_status.append('Fail')
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**********Login Failed_InValidData***Test-Passed********")
                    test_status.append('Pass')
                elif self.exp == 'Fail':
                    self.logger.info("**********Login Failed_ValidData***Test-Failed********")
                    test_status.append('Pass')
        if "Fail" not in test_status:
            self.logger.info("**********Login Test DDT *** Passed ********")
            self.driver.close()
            assert True
        else:
            self.logger.info("**********Login Test DDT *** Failed ********")
            self.driver.close()
            assert False
        self.logger.info("**********END of Login Test DDT ********")
        self.logger.info("**********Completed TC_login DDT ********")

