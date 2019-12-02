import unittest
from courseorder import courses_to_take

class TestCourseOrder(unittest.TestCase):

    def testDiamondExample(self):
        courses = {
            '1': ['2','3'],
            '2': ['3',],
            '3': ['5','4'],
            '5': [],
            '4': ['5']
        }
        self.assertEqual(courses_to_take(courses), ['5','4','3','2','1'])

if __name__ == "__main__":
    unittest.main()

