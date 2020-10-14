import pytest, yaml, os, logging
from dataclasses import dataclass
from datetime import datetime
from abswt.elements import FluentFinder
from abswt.actions import Actions
from selenium import webdriver


DEFAULT_ABS_CONFIG_PATH = os.path.dirname(os.path.realpath(__file__)) + '/config.yaml'
ABS_CONFIG_PATH = os.environ.get('ABS_CONFIG_PATH', DEFAULT_ABS_CONFIG_PATH)


@dataclass
class Config:
    wd_path: str
    find_element_timeout: int
    wait_for_condition_timeout: int
    wait_between: int


@pytest.fixture(scope='session')
def abs_config() -> Config:
    with open(ABS_CONFIG_PATH, 'r', encoding='utf-8') as c:
        data = yaml.load(c, Loader=yaml.FullLoader)
        return Config(**data)


@pytest.fixture(scope='session')
def driver(abs_config):
    driver = webdriver.Chrome(executable_path=abs_config.wd_path)
    driver.maximize_window()
    yield driver

    driver.quit()


@pytest.fixture(scope='session')
def actions(driver, abs_config):
    finder = FluentFinder(webdriver=driver, default_timeout=abs_config.find_element_timeout)
    return Actions(
        finder=finder,
        wait_for_condition_timeout=abs_config.wait_for_condition_timeout,
        wait_between=abs_config.wait_between
    )


@pytest.fixture(scope='session', autouse=True)
def set_abs_logging_levels():
    logging.getLogger('abs-actions').setLevel(logging.INFO)
    logging.getLogger('abs-finder').setLevel(logging.DEBUG)
