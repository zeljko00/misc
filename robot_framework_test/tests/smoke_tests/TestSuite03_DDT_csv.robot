*** Settings ***
Documentation    DDT based test suite!
Library          DataDriver    ../../test_data/testSuite03_data.csv
Test Template    Log Info


*** Test Cases ***    VALUE1    VALUE2    
Log Data              ${val1}   ${val2}    

*** Keywords ***
Log Info   
    [Arguments]       ${val1}   ${val2}
    Log               ${val1} ${val2}     
