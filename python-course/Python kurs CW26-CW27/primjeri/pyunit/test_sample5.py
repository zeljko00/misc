import unittest
from widget.widget import Widget


class DefaultWidgetSizeTestCase(unittest.TestCase):
    def runTest(self):
        widget = Widget("The widget")
        assert widget.size() == (50, 50)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(DefaultWidgetSizeTestCase("testDefaultSize"))
    suite.addTest(DefaultWidgetSizeTestCase("testResize"))
    return suite

if __name__ == '__main__':

    suite = unittest.makeSuite(DefaultWidgetSizeTestCase,'test')
    # suite1 = module1.TheTestSuite()
    # suite2 = module2.TheTestSuite()
    alltests = unittest.TestSuite((suite))
    runner = unittest.TextTestRunner()
    runner.run(alltests)

    #unittest.main()
