from abswt.pages import Page
from abswt.elements import Locator, Using
from abswt.conditions import XpathExists


class Search(Page):
    url = 'https://google.pl'
    SEARCH_INPUT = Locator(Using.NAME, 'q')

    def search_for(self, text: str) -> None:
        self.actions.type_text(self.SEARCH_INPUT.get_by(), text=text)
        self.actions.submit()
        self.actions.wait_for(XpathExists('//div[@id="search"]'))
