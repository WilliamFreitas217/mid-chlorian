import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class User(object):
    username = "newuser616"
    email = "newuser616@testnew.te"
    password = "123456789"


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"/home/william/Documentos/driver/geckodriver")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("Test")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.assertIn("Search Python.org", driver.find_element_by_tag_name("h2").text)

    def test_login(self):
        driver = self.driver
        driver.get("https://hvacnhurry.com")
        elemLogin = driver.find_element_by_xpath("//a[contains(text(),'Log In')]")
        elemLogin.click()
        driver.implicitly_wait(5)
        register = driver.find_element_by_xpath("//*[@id='register-link']")
        register.click()
        elemEmail = driver.find_element_by_xpath("//input[@id='register_email']")
        elemEmail.click()
        elemEmail.send_keys("185erd@test.com")
        elemPwd = driver.find_element_by_xpath("//input[@id='register_pwd']")
        elemPwd.click()
        elemPwd.send_keys("22233385")
        elem_re_Pwd = driver.find_element_by_xpath("//input[@id='register_re_pwd']")
        elem_re_Pwd.click()
        elem_re_Pwd.send_keys("22233385")
        registerBtn = driver.find_element_by_xpath("//form[@id='register-form']/button")
        registerBtn.click()
        driver.implicitly_wait(10)
        elemLogout = driver.find_element_by_xpath("//a[contains(text(),'Log Out')]")
        self.assertIn("LOG OUT", elemLogout.text)

    def test_signup_sucess(self):
        driver = self.driver
        driver.get("https://angularjs.realworld.io/#/register")
        user = User()
        username = driver.find_element_by_xpath("//input[@ng-model='$ctrl.formData.username']")
        username.send_keys(user.username)
        email = driver.find_element_by_xpath("//input[@ng-model='$ctrl.formData.email']")
        email.send_keys(user.email)
        password = driver.find_element_by_xpath("//input[@ng-model='$ctrl.formData.password']")
        password.send_keys(user.password)
        signup = driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right ng-binding']")
        signup.click()
        time.sleep(10)
        self.assertIn(user.username, driver.find_elements_by_xpath("//a[@class='nav-link ng-binding']")[0].text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
