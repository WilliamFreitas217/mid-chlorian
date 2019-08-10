from conftest import *
import time


class WriteArticle(TestTemplate):

    def test_write_new_article(self):
        signin_page = SigninPage(self.driver)
        home_page = Home(self.driver)
        article = NewArticle(self.driver)
        post = ArticlePost(self.driver)
        home_page.go_to_sign_in()
        signin_page.set_email(User.email)
        signin_page.set_pass(User.password)
        signin_page.sign_in()
        time.sleep(5)
        assert home_page.is_in_page()
        home_page.go_to_new_article()
        article.enter_title(title='Eae, man')
        article.enter_about(about='Ricardo Millos')
        article.enter_article(article="no, God. Please. No!")
        article.enter_tags(tags='memes')
        article.publish_article()
        time.sleep(5)
        assert post.is_in_page()
