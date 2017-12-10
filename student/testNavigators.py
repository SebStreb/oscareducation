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

loginStudent = "eleve.eleve"
pwd = "eleve"



class TestNavigator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
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

    # We surf simply with Chrome
    def testSurfChrome(self):
        driver = self.driver
        driver.get(self.base_url + "professor/dashboard/")
        self.driver.find_element_by_xpath("//a[@href='/professor/lesson/134/']").click()
        driver.find_element_by_id("id_my_tests_button").send_keys(Keys.ENTER)
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/add/")
        driver.find_element_by_xpath("//a[@href='/professor/lesson/134/test/online/add/']").click()
        time.sleep(5)


    # We create a question
    def testCreateQuestion(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/online/add/")
        driver.find_element_by_id("test_name").send_keys("Test avec Chrome")
        time.sleep(2)
        driver.find_element_by_id("addSkillToTestButtonForStage9").click()
        time.sleep(3)
        driver.find_element_by_id("id_create_test_button").send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath("(//a[@class='btn btn-primary btn-xs'])[3]").send_keys(Keys.ENTER)

        Select(driver.find_element_by_xpath("//li/div/div/div/select")).select_by_visible_text(u"Question à trous")
        driver.find_element_by_xpath("(//form/ul/li/div/div/div/textarea)[1]").send_keys("filling1")
        driver.find_element_by_css_selector("button.btn.btn-success").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//textarea").send_keys("enonce")
        element = driver.find_element_by_id("parserField")
        element.send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("answers")
        driver.find_element_by_xpath("(//form/ul/li/div/div/div/textarea)[1]").send_keys("filling2")
        driver.find_element_by_xpath("(//form/ul/li/div/div/div/textarea)[2]").send_keys("Source")
        driver.find_element_by_xpath("//form/ul/li/div/div/div/input").send_keys("Indication ")
        time.sleep(4)
        driver.find_element_by_id("validate-yaml").send_keys(Keys.ENTER)
        driver.find_element_by_id("submit-pull-request").send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_link_text(u"Accéder au récapitulatif du test").send_keys(Keys.ENTER)
        time.sleep(5)

    # We answer to a question
    def testAnswerQuestion(self):
        driver = self.driver
        driver.get(self.base_url + "accounts/logout/")
        driver.get(self.base_url + "accounts/usernamelogin/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("eleve.eleve")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("eleve")
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        time.sleep(5)
        driver.find_element_by_xpath("(//a[@class='list-group-item'])[last()]").send_keys(Keys.ENTER)
        time.sleep(2)
        elem = driver.find_element_by_xpath("//form/div/div/input").send_keys(5)
        time.sleep(1)
        driver.find_element_by_xpath("//form").submit()
        time.sleep(2)
        driver.get(self.base_url + "accounts/logout/")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


