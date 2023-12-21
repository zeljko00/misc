print("__name__ printed from main-module:",__name__)
from test_module import f as ff
import test_package.first_module

# checking if module is run directly, not imported
# equivalent to main method in other programming languages
if __name__=="__main__":
    ff()
    test_package.first_module.f()