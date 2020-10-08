import pytest
from abswt.actions import Actions
from libs.google import Search

@pytest.mark.google
@pytest.mark.parametrize("text", [
    "bigSAS github",
    "dr disrespect"
])
def test_google_search(actions: Actions, text: str):
    search = Search(actions)
    search.open()
    search.search_for(text)
    title = search.title
    assert text in title
