import pytest
import requests
#from robot.api.deco import library
#from robot.api.deco import keyword

#@keyword
def test_that_passes()
    logger.debug("Test 1")
    response = requests.get('https://volvocars.com')
    assert(response.status_code == 200)
    
#@keyword
def test_that_fails()
    logger.debug("Test 2")
    response = requests.get('https://volvoocars.com')
    assert(response.status_code == 200)

def test_using_fixtures_pass(just_dial)
    logger.debug("Test 3")
    assert(response.status_code==200)

def test_using_fixtures_fail(wrong_number)
    logger.debug("Test 4")
    assert(response.status_code==200)








