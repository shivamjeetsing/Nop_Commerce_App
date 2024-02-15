import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select

class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitemAdministrators_xpath = "//span[normalize-space()='Administrators']"
    lstitemRegistered_xpath = "//span[normalize-space()='Registered']"
    lstitemGuests_xpath = "//span[normalize-space()='Guests']"
    lstitemVendors_xpath = "//span[normalize-space()='Vendors']"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"
    multiselect_item="//select[@id='SelectedCustomerRoleIds']"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element('xpath',self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element('xpath',self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element('xpath',self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element('xpath',self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element('xpath',self.txtPassword_xpath).send_keys(password)

    # def setCustomerRoles(self,role):
    #     self.driver.find_element('xpath',self.txtcustomerRoles_xpath).click()
    #     st_dropdown=Select(self.driver.find_element('xpath',self.multiselect_item))
    #     time.sleep(3)
    #     if role == 'Registered':
    #         st_dropdown.select_by_value("Registered")
    #         #self.listitem = self.driver.find_element('xpath',self.lstitemRegistered_xpath)
    #     elif role=='Administrators':
    #         st_dropdown.select_by_index("0")
    #         #self.listitem=self.driver.find_element('xpath',self.lstitemAdministrators_xpath)
    #     elif role=='Guests':
    #         # Here user can be Registered( or) Guest, only one
    #         time.sleep(3)
    #         self.driver.find_element('xpath',"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
    #         self.listitem = self.driver.find_element('xpath',self.lstitemGuests_xpath)
    #     elif role=='Registered':
    #         self.listitem = self.driver.find_element('xpath',self.lstitemRegistered_xpath)
    #     elif role=='Vendors':
    #         self.listitem = self.driver.find_element('xpath',self.lstitemVendors_xpath)
    #     else:
    #         self.listitem = self.driver.find_element('xpath',self.lstitemGuests_xpath)
    #     time.sleep(3)
    #     #self.listitem.click()
    #     self.driver.execute_script("arguments[0].click();", self.listitem) # write java script for click function. some time click is not working.

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element('xpath',self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element('id',self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element('id',self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element('id',self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element('xpath',self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element('xpath',self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element('xpath',self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element('xpath',self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element('xpath',self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element('xpath',self.btnSave_xpath).click()
        time.sleep(5)