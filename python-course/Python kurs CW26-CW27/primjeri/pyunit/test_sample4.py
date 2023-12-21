import unittest
from widget.widget import Widget


class DefaultWidgetSizeTestCase(unittest.TestCase):
    def runTest(self):
        widget = Widget("The widget")
        assert widget.size() == (50, 50)


if __name__ == '__main__':
    #  unittest.main()
    testCase = DefaultWidgetSizeTestCase()
    runner = unittest.TextTestRunner()
    runner.run(testCase)
