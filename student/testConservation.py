# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

login = "eleve.eleve"
pwd = "eleve"

loginProf = "prof"
pwdProf = "prof"


# Simple question
tests = [{"nomDuTest" : "Test de Pythagore 3", "enonce" : "Soit un triangle rectangle dont un est des cotes adjacents est de 3cm, et l'autre de 4 cm, combien de cm mesure l'hypothenuse ? (Reponse uniquement en nombres)","title":"Theoreme de Pytahgore","filling":"L'hypothenuse mesure","filling2": "cm","answers":"5","sources":"LINGI2255"}]

# Double question
tests2 = []

# Placeholders
tests3 = []


#test_id = 24
class TestPersistance(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(2)
        self.base_url = "http://127.0.0.1:8000/"
        self.login = loginProf
        self.pwd = pwdProf


    """def testQuest(self):

        driver = self.driver
        driver.get(self.base_url + "accounts/usernamelogin/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(login)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(pwd)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()

        driver.get("http://127.0.0.1:8000/student/test/732/")
        elem = driver.find_element_by_xpath("//form/div/div/input")
        print(elem)
        elem.send_keys("5")
        time.sleep(5)"""

    # Creation of question
    def testCreationQuestion(self):
        driver = self.driver
        # Connection to prof account
        driver.get(self.base_url + "accounts/usernamelogin/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(loginProf)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(pwdProf)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()

        # Click doesn't work, we have to enter the address probably because it's not a link with <a> but a javascript function.
        driver.find_element_by_xpath("//a[@href='/professor/lesson/134/']").click()
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/add/")
        driver.find_element_by_xpath("//a[@href='/professor/lesson/134/test/online/add/']").click()
        # We select a test content
        test = tests[0]
        driver.find_element_by_id("test_name").send_keys(test.get("nomDuTest"))
        time.sleep(5)
        driver.find_element_by_id("addSkillToTestButtonForStage9").click()
        time.sleep(5)
        elem = driver.find_element_by_id("test_name")

        time.sleep(5)
        driver.find_element_by_id("id_create_test_button").send_keys(Keys.ENTER)
        time.sleep(10)
        driver.find_element_by_xpath("(//a[@class='btn btn-primary btn-xs'])[3]").send_keys(Keys.ENTER)
        #driver.find_element_by_link_text(u"nouveau").send_keys(Keys.ENTER)
        #driver.find_element_by_id("exercice-html").send_keys(test.get("enonce"))


        #elem.send_keys(test.get("enonce"))

        time.sleep(10)
        driver.find_element_by_xpath("//form/ul/li/div/div/div/input").send_keys(test.get("filling"))
        Select(driver.find_element_by_xpath("//li/div/div/div/select")).select_by_visible_text(u"Question à trous")
        driver.find_element_by_css_selector("button.btn.btn-success").send_keys(Keys.ENTER)
        #driver.find_element_by_xpath("//textarea").send_keys(
            #"Soit un triangle rectangle dont un est des cotes adjacents est de 3cm, et l'autre de 4 cm, combien de cm mesure l'hypothenuse ? (Reponse uniquement en nombres)")
        driver.find_element_by_xpath("//textarea").send_keys(test.get("enonce"))
        elem = driver.find_element_by_id("exercice-html")
        print(test.get("enonce"))
        element = driver.find_element_by_id("parserField")
        element.send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys(test.get("answers"))
        driver.find_element_by_xpath("(//form/ul/li/div/div/div/textarea)[1]").send_keys(test.get("filling2"))
        driver.find_element_by_xpath("(//form/ul/li/div/div/div/textarea)[2]").send_keys("Source")
        driver.find_element_by_xpath("//form/ul/li/div/div/div/input").send_keys("Indication")
        time.sleep(5)
        driver.find_element_by_id("validate-yaml").send_keys(Keys.ENTER)
        driver.find_element_by_id("submit-pull-request").send_keys(Keys.ENTER)

        driver.find_element_by_link_text(u"Accéder au récapitulatif du test").send_keys(Keys.ENTER)
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/")
        driver.find_element_by_xpath("//table/tbody/tr/td/form/button").send_keys(Keys.ENTER)
        driver.switch_to.alert.accept()
        driver.get(self.base_url + "accounts/logout/")

        print("test created")

        time.sleep(2)
        driver = webdriver.Firefox()
        test = tests[0]
        driver.get(self.base_url + "accounts/usernamelogin/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(login)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(pwd)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        # driver.find_element_by_link_text(test.get("nomDuTest")).send_keys(Keys.ENTER)
        driver.find_element_by_xpath("(//a[@class='list-group-item'])[last()]").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath("//form").submit()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//form/div/div/input")
        print(elem)
        elem.send_keys(test.get("answers"))
        time.sleep(2)
        #rep.send_keys(test.get("answers"))
        driver.find_element_by_xpath("//form").submit()
        time.sleep(2)
        driver.get(self.base_url + "accounts/logout/")

        driver.get(self.base_url + "accounts/usernamelogin/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(loginProf)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(pwdProf)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        time.sleep(100)

    # Test persistance of the question
    """def testPersistanceQuestion(self):



        time.sleep(100)

    # Test the consistence of the enonce of the question (Is the text of the question the same that the text in creatting question
    def testQuestionConsistence(self):
        print("")

    # Test if the response has been transmitted correctly and if it's correct.
    def testAnswersPersistance(self):
        print("")

    def testPersistance(self):
        driver = self.driver

        # Connection
        driver.get(self.base_url + "accounts/usernamelogin/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(loginProf)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(pwdProf)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()

        # Click doesn't work, we have to enter the address probably because it's not a link with <a> but a javascript function.
        driver.find_element_by_xpath("//a[@href='/professor/lesson/134/']").click()
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/add/")
        driver.find_element_by_xpath("//a[@href='/professor/lesson/134/test/online/add/']").click()
        # We select a test content
        test = tests[0]
        driver.find_element_by_id("test_name").send_keys(test.get("nomDuTest"))
        driver.find_element_by_id("addSkillToTestButtonForStage9").click()
        elem = driver.find_element_by_id("test_name")

        # Here the click doesn't work too
        try:
            driver.find_element_by_id("id_create_test_button").click()

        except:
            print("fail")




        # The click doesn't works
        elem.send_keys(Keys.ENTER)
        driver.execute_script('document.getElementById("id_create_test_button").click();')
        print(driver.current_url)
        wait = WebDriverWait(driver, 10)
        print(driver.current_url)


        # We pass directly to the question form creation.
        driver.get(self.base_url + "professor/exercices/validation_form/#?for_test_exercice=14&code=S41eII")

        driver.find_element_by_id("exercice-html")
        elem = driver.find_element_by_id("exercice-html")
        elem.send_keys(test.get("enonce"))


        elem2 = driver.find_element_by_xpath("//form/ul/li/div/div/div/input")
        elem2.send_keys(test.get("filling"))
        self.assertEqual(driver.find_element_by_xpath("//form/ul/li/div/div/div/input").get_attribute('value'),
                         test.get("filling"))
        Select(driver.find_element_by_xpath("//li/div/div/div/select")).select_by_visible_text(u"Question à trous")
        driver.find_element_by_css_selector("button.btn.btn-success").send_keys(Keys.ENTER)

        element = driver.find_element_by_id("parserField")
        element.send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys(test.get("answers"))
        time.sleep(10)
        driver.find_element_by_xpath("(//form/ul/li/div/div/div/textarea)[1]").send_keys(test.get("filling2"))

        elem3 = driver.find_element_by_xpath("(//form/ul/li/div/div/div/textarea)[2]")
        elem3.send_keys("Source")

        elem4 = driver.find_element_by_xpath("//form/ul/li/div/div/div/input")
        elem4.send_keys("Indication")
        time.sleep(15)

        driver.find_element_by_id("validate-yaml").send_keys(Keys.ENTER)
        time.sleep(10)
        driver.find_element_by_id("submit-pull-request").send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_link_text(u"Accéder au récapitulatif du test").send_keys(Keys.ENTER)
        time.sleep(10)
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/")
        driver.find_element_by_xpath("//table/tbody/tr/td/form/button").send_keys(Keys.ENTER)
        time.sleep(5)
        driver.switch_to.alert.accept()
        time.sleep(20)
        driver.get(self.base_url + "accounts/logout/")

    def testQuestion(self):
        driver = self.driver
        test = tests[0]
        driver.get(self.base_url + "accounts/usernamelogin/")
        driver.get(self.base_url + "accounts/usernamelogin/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(login)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(pwd)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        print(driver.current_url)
        # div[@id='content']//table//tr[last()]//td[contains(text(),'service')][last()]/following-sibling::td[2]
        driver.find_element_by_xpath("//div/div/div/div/a[last()]/span").click()
        print(driver.current_url)
        #driver.find_element_by_xpath("//div/div/div/div/a[last()]/").send_keys(Keys.ENTER)
        #print(driver.current_url)
        #driver.find_element_by_link_text(test.get("nomDuTest")).click()
        driver.find_element_by_class_name("list-group-item")
        driver.find_element_by_xpath("(//a[@class='list-group-item'])[last()]").send_keys(Keys.ENTER)
        #driver.find_element_by_xpath("//button[@type='submit']").send_keys(Keys.ENTER)




        time.sleep(7)"""
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


