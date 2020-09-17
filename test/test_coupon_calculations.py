import unittest
from store import coupon_calculations as coupon

class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(6.89, coupon.calculate_price(5.99, 5, 10), 2)
        self.assertAlmostEqual(6.84, coupon.calculate_price(5.99, 5, 15), 2)
        self.assertAlmostEqual(6.79, coupon.calculate_price(5.99, 5, 20), 2)
        self.assertAlmostEqual(2.12, coupon.calculate_price(5.99, 10, 10), 2)
        self.assertAlmostEqual(2.34, coupon.calculate_price(5.99, 10, 15), 2)
        self.assertAlmostEqual(2.55, coupon.calculate_price(5.99, 10, 20), 2)


if __name__ == '__main__':
    unittest.main()
