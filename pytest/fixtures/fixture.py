import requests
#from robot.api.deco import library
#from robot.api.deco import keyword



@pytest.fixture
#@keyword
def just_dial():
    response = requests.get('https://volvocars.com')
    return response.status_code

@pytest.fixture
#@keyword
def wrong_number():
    response = requests.get('https://volvoocars.com')
    return response.status_code
