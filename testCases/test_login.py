from pageObject.LoginPage import Login
from utilites.readProperties import ReadConfig
from utilites.customlogger import LogGen

class Test_001_Login:
    baseurl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_homePagetitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver= setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshot\\"+"test_homePagetitle.png")
            self.logger.error("**** Home page title test failed****")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver= setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.logger.info("****Login test passed ****")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshot\\" + "test_login.png")
            self.logger.info("****Login test failed ****")
            self.driver.close()
            assert False

