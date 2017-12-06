# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


login = "prof"
pwd = "prof"



class TestEditing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(2)
        self.base_url = "http://127.0.0.1:8000/"
        self.login = login
        self.pwd = pwd
        self.driver.get(self.base_url + "accounts/usernamelogin/")
        self.driver.find_element_by_id("id_username").clear()
        self.driver.find_element_by_id("id_username").send_keys("prof")
        self.driver.find_element_by_css_selector("input.btn.btn-primary").click()
        self.driver.find_element_by_id("id_password").clear()
        self.driver.find_element_by_id("id_password").send_keys("prof")
        self.driver.find_element_by_css_selector("input.btn.btn-primary").click()
        print(self.driver.current_url)
        """self.driver.find_element_by_xpath("//a[@href='/professor/lesson/134/']").click()
        self.driver.get(self.base_url + "professor/lesson/134/test/")
        self.driver.find_element_by_xpath("//td/a[0]").send_keys(Keys.ENTER)"""

#)



    def testCorrectAnswers(self):
        driver = self.driver
        driver.get(self.base_url + "professor/lesson/134/student/1137/test/25/")

        self.driver.find_element_by_class_name("answers-table")
        elem = self.driver.find_element_by_xpath("//td[@class='right-border']").text
        elem2 = self.driver.find_element_by_xpath("//td[@width='50%']").text
        #elem2 = self.driver.find_element_by_xpath("(//tr)[1]").text
        print(elem)
        print(elem2)
        #self.driver.find_element_by_xpath("//a[@href='/professor/lesson/134/']")
        self.assertEqual(elem,elem2)
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


