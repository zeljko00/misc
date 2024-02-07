*** Settings ***
Name             First Test Suite!

Metadata         KEY    VALUE
Documentation    My first .robot file!
# library import (in this case it wasn't necessary, because built-in libraries are imported by default)
Library          Collections
# resource file import
Resource         ../../resources/keywords01.resource
# variable file import
Resource         ../../resources/var.resource
# test suit setup logic
Suite Setup      Test Suite Setup
# test suit teardown logic
Suite Teardown   Test Suite Teardown
# default test case setup logic
Test Setup       Default Setup
# default test case teardown logic
Test Teardown    Default Teardown
# tagging all tests cases in this test suite file
Default Tags     suite01

# Test Template
# Test Timeout

*** Variables ***
# user defined variables
${framework}        Robot framework
${key}              yoghurt
${count}            14
*** Test Cases ***
TestCase01
    [Documentation]            My 1st test in ${framework}!
    ...                        ${key}
    ...                        *bold text*
    ...                        _italic text_
    ...                        Rest of documentation...
    [tags]                     success
    [Setup]                    Test Case Setup
    [Teardown]                 Test Case Teardown

    @{list} =  Prepare List    apple     bannana    pear    grapes
    Append To List             ${list}   yoghurt   milk
    Containes                  ${key}    @{list}    

TestCase02
    [Documentation]            My 2nd test in ${framework}!
    ...                        Rest of documentation...
    [tags]                     fail

    @{list} =  Prepare List    apple    bannana    pear    grapes
    Append To List             ${list}  yoghurt   milk
    Containes                  key      @{list}   

TestCase03
    [Documentation]            My 3rd test in ${framework}!
    ...                        Rest of documentation...
    [tags]                     fail

    @{list} =  Prepare List    apple    bannana    pear    grapes    milk    milk
    Occurances                 milk     2          @{list}            
    Occurances                 milk     1          @{list}    
    Occurances                 milk     3          @{list}    

TestCase04
    Keyword01    a    b
    Keyword02    c    d
    Keyword02    f
    Keyword03    1st    2nd    3rd    4th
    Keyword03    1st    2nd    3rd
    Keyword03    1st    2nd
    Keyword03    1st    
    # using named arguments
    Keyword04    first    arg3=third
    ${value} =   Set Variable    VARIABLE
    ${name} =   Set Variable    arg3
    Keyword04    first    ${name}=${value}
    # sends "value" value to Keyword04, not value of variable called value
    Keyword04    first    ${name}=value
    # name=${value} is sent as 2nd positional argument, it is not named argement because there is no
    # argument called "name" in keyword argument list
    Keyword04    first    name=${value}
    # experimenting with varargs and kwargs
    
TestCase05
    @{list} =  Prepare List    apple    bannana    pear    grapes    milk    milk
    FOR    ${var}    IN    @{list}
           # for loop body can have if else statements
           Log    ${var}    
    END

TestCase06
    Keyword05    1st arg
    Keyword05    1st arg        2nd arg 
    Keyword05    1st arg        arg2=2nd arg
    Keyword05    arg1=1st arg   arg2=2nd arg    arg3=3rd arg   arg4=4th args 

TestCase07
    Keyword06    1st arg 
    Keyword05    1st arg    optional arg1
    Keyword05    1st arg    optional arg1    arg3=2nd arg

TestCase08
    @{list} =  Prepare List    apple    bannana    pear    grapes
    Log List     ${list}
    Log List     @{list}

TestCase09
    Keyword09    arg1
    Keyword09    arg1    arg2
    Keyword09    arg1    arg2    arg3
    Keyword09    arg1    arg=value

TestCase10
    Keyword10    arg1    arg=value

TestCase11    
    # explicit test case fail
    Fail         Custom error message ...

TestCase12    
    # explicit test case fail with HTML message
    Fail         *HTML* Custom error message...          
TestCase13
    Log    ${TEST_NAME}
    Keyword13
TestCase${count}
    Log    Test with variable in its name!

TestCase15
    @{locale list} =    Prepare List    item1    item2    item3
    Keyword15           @{locale list}
    # equivalent as following
    # because list sent as @{list name} is expanded and its elements are sent as individual arguments 
    Keyword15           item1    item2    item3

# fails if cmd_var is not set when starting tests 
TestCase16
    Log    ${cmd_var}

TestCase17
    Keyword17 With Embedded (custom embedded value) Value    argument value
*** Keywords ***
# user defined keyword (wrapper for keyword from built in library)



Containes
    [Arguments]                ${value}    @{list}    
    # overriding default failure message
    List Should Contain Value  ${list}    ${value}    msg=Does not contain specified value!

Occurances
    [Arguments]                ${value}    ${expected}    @{list}
    ${count} =                 Count Values in List       ${list}        ${value}             
    Run Keyword If             ${count} == ${expected}    Log    Found expected number of ocurances!
    ...    ELSE IF             ${count} < ${expected}     Log    Found less than expected occurances!
    ...    ELSE                                           Log    Found more than expected occurances!

# keyword accepting 2 positional arguments
Keyword01
    [Arguments]                ${arg1}        ${arg2}
    Log                        1st argument: ${arg1}
    Log                        2nd argument: ${arg2}              
# keyword accepting 2 positional arguments, second with specified default value
Keyword02
    [Arguments]                ${arg1}        ${arg2}=default value
    Log                        1st argument: ${arg1}
    Log                        2nd argument: ${arg2}
# keyword accepting 2 positional arguments, second with specified default value and variable number of parameters as 3rd argument
Keyword03
    [Arguments]                ${arg1}        ${arg2}=default value    @{vararg}
    Log                        1st argument: ${arg1}
    Log                        2nd argument: ${arg2}
    Log List                   ${vararg}
# keyword accepting 3 positional arguments, second and third with specified default value
Keyword04
    [Arguments]                ${arg1}        ${arg2}=default arg2     ${arg3}=default arg3
    Log                        1st argument: ${arg1}
    Log                        2nd argument: ${arg2}        
    Log                        2nd argument: ${arg3}   
# keyword accepting 1 positional arg and variable number of named args
Keyword05
    [Arguments]                ${arg1}        ${arg2}=default arg2      &{kwargs}    
    Log                        ${arg1}
    Log                        ${arg2}
    Log                        ${kwargs}

Keyword06
    [Arguments]                ${arg1}        @{varargs}    &{kwargs}    
    Log                        ${arg1}
    Log List                   ${varargs}
    Log                        ${kwargs}

Keyword09
    [Arguments]                @{varargs}     ${arg}=default arg value
    Log List                   ${varargs}        
    Log                        ${arg}

Keyword10
    [Arguments]                @{varargs}     ${arg}
    Log List                   ${varargs}        
    Log                        ${arg}
    
Keyword13
    Log                        ${TEST_NAME}
Keyword15
    [Arguments]    @{list}
    Log List    ${list}
# keyword with argument embedded in its name
Keyword17 With Embedded (${value}) Value
    [Arguments]    ${arg}
    Log Many    ${value}    ${arg}