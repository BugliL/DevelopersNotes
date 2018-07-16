import unittest


class Year(object):

    def __init__(self, year):
        self.year = year

    def isLeap(self):
        return self.isDivisibleBy(4) and not self.isDivisibleBy(100) or self.isDivisibleBy(400)

    def isDivisibleBy(self, n):
        return self.year % n == 0


class Test1(unittest.TestCase):

    # Test list
    # - typical year 1996
    # - atypical common year

    def test_itWorks(self):
        self.assertTrue(True)

    def test_tipicalLeapYear(self):
        # Test fatto da 3 fasi distinte

        # arrange
        year = Year(1996)

        # act
        isLeap = year.isLeap()

        # assert
        self.assertTrue(isLeap)

    def test_atypicalCommonYear(self):
        year = Year(1900)

        isLeap = year.isLeap()

        self.assertFalse(isLeap)

    def test_typicalLeapYear(self):

        year = Year(2000)

        isLeap = year.isLeap()

        self.assertTrue(isLeap)
#
# if __name__ == "__main__":
#     unittest.main()
