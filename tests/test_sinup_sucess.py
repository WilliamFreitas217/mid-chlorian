from conftest import *
import time


class TestSignup(TestTemplate):

    def test_signup_success(self):
        signup_page = SignupPage(self.driver)
        signup_page.set_user(User.username)
        signup_page.set_email(User.email)
        signup_page.set_pass(User.password)
        signup_page.signup()
        time.sleep(10)
        self.assertEqual(User.username, Home.signup_check())
