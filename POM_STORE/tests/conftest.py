import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/index.html")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()



# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     config.option.allure_report_dir = "allure-results"