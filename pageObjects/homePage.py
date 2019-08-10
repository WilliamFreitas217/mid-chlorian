from basePage import BasePage


class Home(BasePage):
    signed = "//a[@class='nav-link ng-binding']"
    settings = "//a[@href='#/settings']"
    your_feed = "//a[@class='nav-link active']"
    new_article = "//a[@href='#/editor/']"

    def signup_check(self):
        return self._driver.find_elements_by_xpath(self.signed)[0].text

    def is_in_page(self):
        return self._driver.find_elements_by_xpath(self.settings) and \
            self._driver.find_elements_by_xpath(self.your_feed)

    def go_to_new_article(self):
        new_article = self._driver.find_elements_by_xpath(self.new_article)
        new_article.click()
