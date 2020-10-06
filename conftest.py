import pytest, yaml
from dataclasses import dataclass
from abswt.elements import FluentFinder
from abswt.actions import Actions
from selenium import webdriver


@dataclass
class Config:
    wd_path: str
    find_element_timeout: int
    wait_for_condition_timeout: int
    wait_between: int


@pytest.fixture(scope='session')
def config() -> Config:
    with open('example.config.yaml', 'r', encoding='utf-8') as c:
        data = yaml.load(c, Loader=yaml.FullLoader)
        return Config(**data)


@pytest.fixture(scope='session')
def driver(config):
    driver = webdriver.Chrome(executable_path=config.wd_path)
    driver.maximize_window()
    yield driver

    driver.quit()


@pytest.fixture(scope='session')
def actions(driver, config):
    finder = FluentFinder(webdriver=driver, default_timeout=config.find_element_timeout)
    return Actions(
        finder=finder,
        wait_for_condition_timeout=config.wait_for_condition_timeout,
        wait_between=config.wait_between
    )