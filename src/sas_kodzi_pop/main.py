from abswt.pages import Page
from abswt.elements import Locator, Using
from abswt.conditions import XpathExists


class Component(Page): pass  # type alias


class OpenPostButton(Component):
    POST_BUTTON = Locator(Using.XPATH, "//section[@class='{css_class}' and contains(., '{post_title}')]//a[contains(., 'Czytaj dalej')]")

    def click(self, post_title: str) -> None:
        # parameterized selector example + condition override
        self.actions.click(self.POST_BUTTON.get_by(css_class='blog-post', post_title=post_title), condition=EC.visibility_of_element_located)


class SasKodzi(Page):
    """ Sample POP Page """
    url = 'https://sas-kodzi.pl'
    
    BLOG_BUTTON = Locator(Using.XPATH, '//a[@href="/blog"]')
    # POST_BUTTON = Locator(Using.XPATH, "//section[@class='blog-post' and contains(., '{post_title}')]//a[contains(., 'Czytaj dalej')]")

    def goto_posts(self) -> None:
        self.actions.click(self.BLOG_BUTTON.get_by(), timeout=3)
        self.actions.wait_for(XpathExists('//body'))
    
    # def open_post(self, post_title: str) -> None:
    #     self.actions.click(self.POST_BUTTON.get_by(post_title=post_title), condition=EC.visibility_of_element_located)
    #     self.actions.wait_for(XpathExists('//body'), timeout=50)

    def open_post(self, post_title: str) -> None:
        OpenPostButton(self.actions).click(post_title)