from robot.running import TestSuite

def to_json(test_suite,output):
    suite= TestSuite.from_file_system(test_suite)
    suite.adjust_source(relative_to="/directory_containing_test_suite_file")
    # test suit data as json string
    # data=suite.to_json()
    # save te-st suit data in json file
    suite.to_json(output+".rbt",ident=2) 

def from_json(rbt_file):
    suite=TestSuite.from_json(rbt_file)
    # resolves problems with different file systems on different machines
    suite.adjust_source(relative_to="/directory_containing_rbt_file")
    # optional execution
    # suite.run("output.xml")