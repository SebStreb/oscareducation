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



    def testAddTest(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/")
        driver.find_element_by_xpath("//a[@href='/professor/lesson/134/test/add/']").send_keys(Keys.ENTER)
        time.sleep(2)
        self.assertEqual("http://127.0.0.1:8000/professor/lesson/134/test/add/",driver.current_url)

    def testAddCompetence(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/online/add/")
        time.sleep(2)
        driver.find_element_by_id("addSkillToTestButtonForStage9").click()
        wait = WebDriverWait(driver, 10)
        elm = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary selected-skill ng-binding']")))
        self.assertEqual(elm.text,"S41eII")


    def testAddCompetenceSelected(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/online/add/")
        time.sleep(1)
        Select(driver.find_element_by_xpath("//select")).select_by_value("S11aII")
        driver.find_element_by_id("addSkillToTestButtonForStage9").send_keys(Keys.ENTER)
        time.sleep(2)
        wait = WebDriverWait(driver, 10)
        elm = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary selected-skill ng-binding']")))
        self.assertEqual(elm.text,"S11aII")



    def testAdd2competences(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/online/add/")
        time.sleep(1)
        Select(driver.find_element_by_xpath("//select")).select_by_value("S11aII")
        driver.find_element_by_id("addSkillToTestButtonForStage9").send_keys(Keys.ENTER)
        time.sleep(3)
        Select(driver.find_element_by_xpath("//select[@ng-model='stage1SelectedSkill']")).select_by_value("S11aI")
        driver.find_element_by_id("addSkillToTestButtonForStage1").send_keys(Keys.ENTER)
        wait = WebDriverWait(driver, 10)
        elm = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//button[@class='btn btn-primary selected-skill ng-binding'])[1]")))
        elm2 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='btn btn-primary selected-skill ng-binding'])[2]")))
        self.assertEqual(elm.text,"S11aII")
        self.assertEqual(elm2.text, "S11aI")


    def testRemoveCompetence(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/online/add/")
        time.sleep(1)
        Select(driver.find_element_by_xpath("//select")).select_by_value("S11aII")
        driver.find_element_by_id("addSkillToTestButtonForStage9").send_keys(Keys.ENTER)
        time.sleep(3)
        Select(driver.find_element_by_xpath("//select[@ng-model='stage1SelectedSkill']")).select_by_value("S11aI")
        driver.find_element_by_id("addSkillToTestButtonForStage1").send_keys(Keys.ENTER)
        wait = WebDriverWait(driver, 10)
        elm = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='btn btn-primary selected-skill ng-binding'])[1]")))
        elm2 = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='btn btn-primary selected-skill ng-binding'])[2]")))
        driver.find_element_by_xpath("(//button[@class='btn btn-primary selected-skill ng-binding'])[2]").click()
        self.assertEqual(elm.text, "S11aII")


    def testCreateCompetence(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/online/add/")
        time.sleep(2)
        driver.find_element_by_id("addSkillToTestButtonForStage9").click()
        driver.find_element_by_id("test_name").send_keys("Test ang")
        wait = WebDriverWait(driver, 10)
        elm = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='id_create_test_button']")))
        driver.find_element_by_id("id_create_test_button").send_keys(Keys.ENTER)
        print(driver.current_url)
        str = driver.find_element_by_id("display_skill_88").text
        words = str.split(" ")
        self.assertEqual(words[1],"S41eII")
        time.sleep(5)




    def testQuestionsTrous(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/online/add/")
        time.sleep(2)
        driver.find_element_by_id("addSkillToTestButtonForStage9").click()
        driver.find_element_by_id("test_name").send_keys("Test ang")
        wait = WebDriverWait(driver, 10)
        elm = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='id_create_test_button']")))
        driver.find_element_by_id("id_create_test_button").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_xpath("(//a[@class='btn btn-primary btn-xs'])[3]").send_keys(Keys.ENTER)
        time.sleep(5)
        Select(driver.find_element_by_xpath("//li/div/div/div/select")).select_by_visible_text(u"Question à trous")
        wait = WebDriverWait(driver,10)
        elm2 = wait.until(
            EC.presence_of_element_located((By.XPATH,"//button[@title='Ajouter un champ']")))
        print(elm2.text)
        driver.find_element_by_xpath("//button[@title='Ajouter un champ']").send_keys(Keys.ENTER)
        textArea = driver.find_element_by_id("blank-text0")
        time.sleep(5)
        print(textArea.text)


        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


