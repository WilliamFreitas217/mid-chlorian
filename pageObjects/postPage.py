from basePage import BasePage


class ArticlePost(BasePage):
    article_edit = "//a[@class='btn btn-outline-secondary btn-sm']"
    article_delete = "//button[@class='btn btn-outline-danger btn-sm']"

    def is_in_page(self):
        return self._driver.find_elements_by_xpath(self.article_edit) and \
            self._driver.find_elements_by_xpath(self.article_delete)
