from pageObject.LoginPage import Login
from utilites.readProperties import ReadConfig
from pageObject.Addcustomerage import AddCustomer
import random
import string


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class Test_001_Login:
    baseurl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    def test_addCustomer(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        print("Login successfully ")
        # Starting to Add customer
        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()
        # After above step we will add some details
        self.email= random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123@")
        #self.addcust.setCustomerRoles("Administrators")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Shiva")
        self.addcust.setLastName("Rathor")
        self.addcust.setDob("12/21/2023")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("this is for testing.....")
        self.addcust.clickOnSave()
        print("test data adding successfully")
        self.msg = self.driver.find_element("xpath","//div[@class='alert alert-success alert-dismissable']").text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            assert False
        self.driver.close()
