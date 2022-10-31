import requests
import pytest

from robot.api.deco import library
from robot.api.deco import keyword


@pytest.fixture
@keyword
def check_github_api():
    response = requests.get('https://api.github.com')
    code = response.status_code
    return code
    

@pytest.fixture
@keyword
def check_nasa_api():
    response = requests.get('https://api.nasa.gov/')
    code = response.status_code
    return code
    