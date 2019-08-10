from basePage import BasePage


class NewArticle(BasePage):
    article_title = "//input[@placeholder='Article Title']"
    article_about = "//input[@ng-model='$ctrl.article.description']"
    article = "//textarea[@placeholder='Write your article (in markdown)']"
    article_tags = "//input[@placeholder='Enter tags']"
    publish = "//button[@class='btn btn-lg pull-xs-right btn-primary']"

    def enter_title(self, title):
        self._driver.find_element_by_xpath(self.article_title).send_keys(title)

    def enter_about(self, about):
        self._driver.find_element_by_xpath(self.article_about).send_keys(about)

    def enter_article(self, article):
        self._driver.find_element_by_xpath(self.article).send_keys(article)

    def enter_tags(self, tags):
        self._driver.find_element_by_xpath(self.article_tags).send_keys(tags)

    def publish_article(self):
        return self._driver.find_element_by_xpath(self.publish).click()
