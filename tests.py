import unittest
import task
import datetime


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        expected = 50.26548245743669
        self.assertEqual(expected, task.circleArea(4))

    def test4(self):
        expected = 4
        self.assertNotEqual(expected, task.circleArea(4))

    def test5(self):
        expected = (7, 3)
        self.assertEqual(expected, task.firstLast([7, 6, 5, 4, 3]))

    def test6(self):
        expected = datetime.timedelta(days=186)
        self.assertEqual(expected, task.timeBetween((2020, 5, 17), (2019, 11, 13)))


if __name__ == '__main__':
    unittest.main()
