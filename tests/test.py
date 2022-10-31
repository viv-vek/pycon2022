import pytest
import requests
import logging
from robot.api.deco import library
from robot.api.deco import keyword

@keyword
def test_that_passes():
    #self._logger.debug("Test 1")
    response = requests.get('https://api.nasa.gov/')
    assert(response.status_code == 200)
    
@keyword
def test_that_fails():
    #self._logger.debug("Test 2")
    response = requests.get('https://api.github.com')
    assert(response.status_code == 404 or response.status_code == 403 )

@keyword
def test_using_fixtures_pass(check_github_api):
    assert(check_github_api==200)

#@keyword
def test_using_fixtures_fail(check_nasa_api):
    #self._logger.debug("Test 4")
    assert(check_nasa_api==404)








