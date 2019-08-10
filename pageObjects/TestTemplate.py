import unittest
from selenium import webdriver


class TestTemplate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(
            executable_path=r"/home/william/Documentos/driver/geckodriver")
        self.driver.get("https://angularjs.realworld.io/#/")

    def tearDown(self):
        self.driver.quit()
