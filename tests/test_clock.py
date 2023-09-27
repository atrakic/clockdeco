import unittest
from clockdeco import clock


class TestClockDeco(unittest.TestCase):
    def setUp(self):
        self.count = 0

    def test_clock(self):
        @clock
        def a():
            self.count += 1
            return "expected_result"

        self.assertEqual(a(), "expected_result")
        self.assertEqual(self.count, 1)


if __name__ == '__main__':
    unittest.main()
