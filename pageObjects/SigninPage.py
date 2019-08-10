from basePage import BasePage


class SigninPage(BasePage):
    username = "//input[@ng-model='$ctrl.formData.username']"
    email = "//input[@ng-model='$ctrl.formData.email']"
    password = "//input[@ng-model='$ctrl.formData.password']"
    signin_button = "//button[@class='btn btn-lg btn-primary pull-xs-right ng-binding']"

    def set_email(self, mail):
        self._driver.find_element_by_xpath(self.email).send_keys(mail)

    def set_pass(self, password):
        self._driver.find_element_by_xpath(self.password).send_keys(password)

    def sign_in(self):
        return self._driver.find_element_by_xpath(self.signin_button).click()

