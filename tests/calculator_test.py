import unittest

import socialsecurity.calculator as calc


class MyTestCase(unittest.TestCase):
    def test_one(self):
        benefit = calc.benefit_at_67(12000.0)
        self.assertEqual(10800.0, benefit)

    def test_two(self):
        benefit = calc.benefit_at_67(24000.0)
        self.assertEqual(15851.04, benefit)

    def test_three(self):
        benefit = calc.benefit_at_67(100001.0)
        self.assertEqual(37610.31, benefit)

    def test_four(self):
        benefit = calc.benefit_at_67(168000.0)
        self.assertEqual(47810.159999999996, benefit)

    def test_too_large(self):
        with self.assertRaises(ValueError):
            calc.benefit_at_67(300000)


if __name__ == '__main__':
    unittest.main()
