*** Settings ***
Documentation           Test connect to webpage

*** Keywords ***
${CONNECTION_OK}  just dial
${CONNECTION_NOT_OK}  wrong number

*** Test Cases ***
Test Using Fixtures Pass [Arguments] ${CONNECTION_OK}
Test Using Fixtures FAIL [Arguments] ${CONNECTION_NOT_OK}
Test That Passes
Test That Fails