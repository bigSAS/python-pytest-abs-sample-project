import pytest

from abswt.actions import Actions
from libs.sas_kodzi_pop.main import SasKodzi


@pytest.mark.blog
def test_goto_blog(actions: Actions):
    sas_kodzi_page = SasKodzi(actions)
    sas_kodzi_page.open()
    sas_kodzi_page.goto_posts()
    # sas_kodzi_page.open_post('Python od zera pt2 - proste typy danych')