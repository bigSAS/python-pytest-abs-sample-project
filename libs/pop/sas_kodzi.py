from abswt.pages import Page
from abswt.elements import Locator, Using
from abswt.conditions import XpathExists
from abswt import expected_conditions as EC


class Component(Page): pass  # type alias


class OpenPostButton(Component):
    POST_BUTTON = Locator(
        Using.XPATH,
        "//section[@class='{css_class}' and contains(., '{post_title}')]"
        "//a[contains(., 'Czytaj')]"
    )

    def click(self, post_title: str) -> None:
        # parameterized selector example + condition override
        locator = self.POST_BUTTON.get_by(
            css_class='blog-post',
            post_title=post_title
        )
        condition=EC.visibility_of_element_located
        self.actions.click(locator, condition=condition)


class SasKodzi(Page):
    url = 'https://sas-kodzi.pl'
    BLOG_BUTTON = Locator(Using.XPATH, '//a[@href="/blog"]')

    def goto_posts(self) -> None:
        self.actions.click(self.BLOG_BUTTON.get_by(), timeout=3)
        self.actions.wait_for(XpathExists("//h1[@class='blog-list-title']"))

    def open_post(self, post_title: str) -> None:
        OpenPostButton(self.actions).click(post_title)
