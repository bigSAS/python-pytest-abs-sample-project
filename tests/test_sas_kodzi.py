import pytest

from abswt.actions import Actions
from libs.pop.sas_kodzi import SasKodzi
from helpers.assertions import xpath_exsists


@pytest.mark.blog
def test_goto_blog(actions: Actions):
    sas_kodzi_page = SasKodzi(actions)
    sas_kodzi_page.open()
    sas_kodzi_page.goto_posts()
    sas_kodzi_page.open_post('Python string FUN')
    assert xpath_exsists(
        actions.webdriver,
        xpath="//h2[@id='kodzenie-na-stringach']",
        timeout=5
    )
