from selenium.webdriver.support.ui import WebDriverWait
from abswt import expected_conditions as EC


def xpath_exsists(webdriver, xpath: str, timeout: int) -> bool:
    try:
        WebDriverWait(webdriver, timeout)\
            .until(EC.presence_of_element_located(('xpath', xpath)))
        return True
    except:
        return False
