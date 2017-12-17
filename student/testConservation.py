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
idStudent = 1137


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
        time.sleep(20)
        enonce = driver.find_element_by_xpath("//div[@ng-bind-html='htmlRendering']").text

        #Check that the text are conserved in previsualisation
        self.assertEqual(enonce,test.get("enonce"))

        driver.find_element_by_id("submit-pull-request").send_keys(Keys.ENTER)
        time.sleep(20)
        driver.find_element_by_link_text(u"Accéder au récapitulatif du test").send_keys(Keys.ENTER)
        url = driver.current_url
        urlTab = url.split("/")
        idTest = urlTab[len(urlTab)-3]
        print("idTest")
        print(idTest)
        print(url)
        driver.get("http://127.0.0.1:8000/professor/lesson/134/test/")
        driver.find_element_by_xpath("//table/tbody/tr/td/form/button").send_keys(Keys.ENTER)
        driver.switch_to.alert.accept()
        driver.get(self.base_url + "accounts/logout/")
        print("test created")

        #Answering to question
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
        time.sleep(10)
        driver.find_element_by_xpath("(//a[@class='list-group-item'])[last()]").send_keys(Keys.ENTER)
        time.sleep(2)
        url2Tab = driver.current_url.split("/")
        idTest2 = url2Tab[len(url2Tab)-2]
        print(idTest2)
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


        # Check the answer posted by student
        driver.get(self.base_url + "accounts/usernamelogin/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(loginProf)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(pwdProf)
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        driver.get("http://127.0.0.1:8000/professor/lesson/134/student/" + str(idStudent) + "/")
        time.sleep(10)
        #driver.find_element_by_xpath("(//li/a)[last()]").send_keys(Keys.ENTER) # Click on the test passed by the student
        #driver.get("http://127.0.0.1:8000/professor/lesson/134/test/online/" + idTest + "/")
        print("dd")
        print(driver.current_url)
        print(idTest2)
        driver.get("http://127.0.0.1:8000/professor/lesson/134/student/"+str(idStudent)+"/test/"+ str(idTest2)+ "/")
        print(driver.current_url)
        time.sleep(10)
        textContent = driver.find_element_by_class_name("exercice-content").text
        self.assertEqual(test.get("enonce"),textContent)
        reponse = driver.find_element_by_xpath("//td[@width='50%'][@class='right-border']").text
        self.assertEqual(reponse,test.get("answers"))
        time.sleep(100)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


