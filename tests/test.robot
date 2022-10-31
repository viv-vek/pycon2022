*** Settings ***
Library      test.py
Library      conftest.py


*** Test Cases ***
Happy Test
  Test That Passes 
Negative Test
  Test That Fails
#Supposed To Be Happy Test
  Test Using Fixtures Pass    check_github_api


      