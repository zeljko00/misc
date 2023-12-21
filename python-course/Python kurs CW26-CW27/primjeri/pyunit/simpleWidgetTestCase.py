import unittest
from widget.widget import Widget


class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget("The widget")

    def tearDown(self):
        self.widget.dispose()
        self.widget = None


class DefaultWidgetSizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        assert self.widget.size() == (50, 50)


class WidgetResizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        self.widget.resize(100, 150)
        assert self.widget.size() == (100, 150)
