import time
import unittest
# import requests
# from requests import Response
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
# import pytest
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class test(unittest.TestCase):
    def setUp(self):
        chrome_opt = webdriver.ChromeOptions()
        prefs = {"credentials_enable_service": False,
                 "profile.password_manager_enabled": False,
                 "profile.default_content_setting_values.geolocation": False}
        chrome_opt.add_experimental_option("prefs", prefs)
        chrome_opt.add_argument("--incognito")
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(options=chrome_opt, service=service)
        driver = self.driver
        driver.get('https://staging.d1ek5b07lygjly.amplifyapp.com/')
        self.assertIn("Cogncise", driver.title)
        time.sleep(3)

    @pytest.mark.order1
    def test_Newlogin(self):
        driver = self.driver
        # Enter User ID
        driver.find_element(By.NAME, 'email').send_keys("cog-auto-test@yopmail.com")
        time.sleep(3)
        # Enter Password
        driver.find_element(By.NAME, 'password').send_keys("d1affqb")
        driver.implicitly_wait(3)
        # Click Login Button
        login = driver.find_element(By.XPATH, '//button[@type="submit"]')
        time.sleep(3)
        login.click()
        driver.implicitly_wait(5)
        print('login to New password page Successfully')
        time.sleep(3)
        # Create New Password
        # Enter new Password
        driver.find_element(By.NAME, 'password').send_keys("Password@123")
        driver.implicitly_wait(3)
        time.sleep(3)
        # Confirm New Password
        driver.find_element(By.NAME, 'confirm_password').send_keys("Password@123")
        driver.implicitly_wait(3)
        print('password entered')
        time.sleep(3)
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(3)
        print('Password Change Succefully')
        # login with new Password

    @pytest.mark.order3
    def test_loginNewPassword(self):
        driver = self.driver
        # Enter User ID
        driver.find_element(By.NAME, 'email').send_keys("cog-auto-test@yopmail.com")
        time.sleep(3)
        # Enter Password
        driver.find_element(By.NAME, 'password').send_keys("Password@123")
        driver.implicitly_wait(3)
        # Click Login Button
        newlogin = driver.find_element(By.XPATH, '//button[@type="submit"]')
        newlogin.click()
        driver.implicitly_wait(5)
        print('LoggedIn with new password Successfully')
        time.sleep(5)

        menu_list = driver.find_element(By.XPATH, '//nav[@class="pro-menu"]')

        # Get the list of menu options
        options = menu_list.find_elements(By.TAG_NAME, "li")

        # Click on the 2nd option
        options[1].click()

        time.sleep(5)

        leads = driver.find_element(By.XPATH, '//button[@class="p-button p-component createlead-btn"]')
        leads.click()
        time.sleep(3)

        firstname = driver.find_element(By.NAME, 'first_name')
        firstname.send_keys("Rahul")
        assert firstname.get_attribute("value") == "Rahul"
        time.sleep(3)

        lastname = driver.find_element(By.NAME, 'last_name')
        lastname.send_keys("Test")
        time.sleep(3)

        mobilenumber = driver.find_element(By.CLASS_NAME, 'form-control ')
        mobilenumber.send_keys("04123456789")
        time.sleep(3)

        Email = driver.find_element(By.NAME, 'email')
        Email.send_keys("Rahul@test.com")
        time.sleep(3)

        # Address
        sreachplace = driver.find_element(By.XPATH, '//input[@type="text"] [@autocomplete="off"]')
        # Enter text in the autocomplete field
        sreachplace.send_keys("Australia")
        time.sleep(3)
        # Wait for the autocomplete options to appear

        # Wait for the autocomplete dropdown container to appear

        wait = WebDriverWait(driver, 10)
        autocomplete_options = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".autocomplete-dropdown-container div")))
        # Select the first autocomplete option
        # autocomplete_options[1].click()
        # assert sreachplace.get_attribute("value") == "Australia"
        try:
            # Select the first autocomplete option
            autocomplete_options[1].click()
        except IndexError:
            # Handle the case where there are no options available
            print("No options available")
        time.sleep(3)

        buildingname = driver.find_element(By.NAME, 'address.building_number')
        buildingname.send_keys("25")
        time.sleep(3)

        levelno = driver.find_element(By.NAME, 'address.level_number')
        levelno.send_keys("4")
        time.sleep(3)

        unittype = driver.find_element(By.NAME, 'address.unit_type')
        unittype.send_keys("unit")
        time.sleep(3)

        unitnumber = driver.find_element(By.NAME, 'address.unit_number')
        unitnumber.send_keys("21")
        time.sleep(3)

        lotno = driver.find_element(By.NAME, 'address.lot_number')
        lotno.send_keys("34")
        time.sleep(3)

        streetnumber = driver.find_element(By.NAME, 'address.street_number')
        streetnumber.send_keys("Street 123")
        time.sleep(3)

        streetname = driver.find_element(By.NAME, 'address.street_name')
        streetname.send_keys("India")
        time.sleep(3)

        streettype = driver.find_element(By.NAME, 'address.street_type')
        streettype.send_keys("Single Street")
        time.sleep(3)

        suffix = driver.find_element(By.NAME, 'address.suffix')
        suffix.send_keys("Testsufix")
        time.sleep(3)

        suburb = driver.find_element(By.NAME, 'address.suburb')
        suburb.send_keys("Testsubrb")
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        autocomplete_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@aria-label="Select State"]')))
        # select the desired option from the list
        state = autocomplete_options[0]
        # perform the click action on the option
        state.click()
        statelist = driver.find_element(By.XPATH, '//div[@class="p-dropdown-items-wrapper"]')
        # Get the list of menu options
        selectstate = statelist.find_elements(By.TAG_NAME, "li")
        # Click on the 2nd option
        selectstate[1].click()
        time.sleep(3)

        pincode = driver.find_element(By.NAME, 'address.pincode')
        pincode.send_keys("12345")
        time.sleep(3)

        lga = driver.find_element(By.NAME, 'address.lga')
        lga.send_keys("lga")
        time.sleep(3)

        #Lead Status
        time.sleep(4)
        wait = WebDriverWait(driver, 10)
        autocomplete_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@aria-label="Select Status"]')))
        # select the desired option from the list
        leadstatus = autocomplete_options[0]
        # perform the click action on the option
        leadstatus.click()
        leadstatuslist = driver.find_element(By.XPATH, '//div[@class="p-dropdown-items-wrapper"]')
        # Get the list of menu options
        selectleadstatus = leadstatuslist.find_elements(By.TAG_NAME, "li")
        # Click on the 2nd option
        selectleadstatus[3].click()
        time.sleep(3)

        #LeadSource
        time.sleep(4)
        wait = WebDriverWait(driver, 10)
        autocomplete_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@aria-label="Select Source"]')))
        # select the desired option from the list
        leadSource = autocomplete_options[0]
        # perform the click action on the option
        leadSource.click()
        leadSourcelist = driver.find_element(By.XPATH, '//div[@class="p-dropdown-items-wrapper"]')
        # Get the list of menu options
        selectstate = leadSourcelist.find_elements(By.TAG_NAME, "li")
        # Click on the 2nd option
        selectstate[1].click()
        time.sleep(3)

        createlead = driver.find_element(By.XPATH, '//button[@aria-label="Create Lead"] [@type="submit"]')
        createlead.click()
        time.sleep(10)

    def tearDown(self):
       self.driver.quit()


if __name__ == '__main__':
    unittest.main()
