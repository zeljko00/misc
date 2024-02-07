*** Settings ***
Documentation    DDT based test suite!
Library          Collections
Test Template    Log Info

*** Variables ***
@{list1}    1    2    3    4    5
@{list2}    11   22   33   44   55
*** Test Cases ***    VALUE    
# first way - template specified in Settings section
Log String            Hello    
Log Number            10       
Log Default           ${EMPTY}
Log Number Second
    10000
# executing template keyword multiple times in same test case:
# keyword failure won't stop test case execution  

# second way - template specified in test case settings 
Log List
    [Template]        Log List Var
    # Log List Var template keyword is executed 2 times
    @{list1}
    @{list2}
# executes template keyword multiple times in same test
Log Info Multiple
    FOR    ${item}    IN    @{list1}
        ${item}
    END    
# executes template keyword multiple times in same test
Log Info Multiple Filtered
    FOR    ${item}    IN    @{list1}
        IF    ${item} > 2
            ${item}
        END
    END    
*** Keywords ***
Log Info   
    [Arguments]       ${val}
    Log               ${val}    
Log List Var
    [Arguments]       @{list}
    Log List          ${list}