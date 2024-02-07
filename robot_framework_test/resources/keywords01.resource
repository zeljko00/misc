*** Settings ***
Library    BuiltIn

*** Variables ***
*** Keywords ***
Test Suite Setup
    Log                       Setting everything up for test suite!
Test Case Setup
    Log                       Setting everything up for test case!
Default Setup
    Log                       Setting everything up!
Test Suite Teardown
    Log                       Cleaning up after test suite!
Test Case Teardown
    Log                       Cleaning up after test case!
Default Teardown
    Log                       Cleaning up!
Prepare List
    [Documentation]           Creates new list and inserts specified elements!
    # accepts variable number of arguments
    [Arguments]               @{items}
    # all received arguments are forwarded to another keyword
    @{list} =  Create List    @{items}
    # returns result value
    RETURN                    ${list}
    # deprecated way
    # [Return]                  @{list} 

