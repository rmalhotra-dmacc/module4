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

    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(27.02, coupon.calculate_price(24.99, 5, 10), 2)
        self.assertAlmostEqual(25.96, coupon.calculate_price(24.99, 5, 15), 2)
        self.assertAlmostEqual(24.90, coupon.calculate_price(24.99, 5, 20), 2)
        self.assertAlmostEqual(22.25, coupon.calculate_price(24.99, 10, 10), 2)
        self.assertAlmostEqual(21.46, coupon.calculate_price(24.99, 10, 15), 2)
        self.assertAlmostEqual(20.66, coupon.calculate_price(24.99, 10, 20), 2)

    def test_price_under_between_thirty_fifty(self):
        self.assertAlmostEqual(50.10, coupon.calculate_price(44.99, 5, 10), 2)
        self.assertAlmostEqual(47.98, coupon.calculate_price(44.99, 5, 15), 2)
        self.assertAlmostEqual(45.86, coupon.calculate_price(44.99, 5, 20), 2)
        self.assertAlmostEqual(45.33, coupon.calculate_price(44.99, 10, 10), 2)
        self.assertAlmostEqual(39.48, coupon.calculate_price(44.99, 10, 15), 2)
        self.assertAlmostEqual(37.62, coupon.calculate_price(44.99, 10, 20), 2)


if __name__ == '__main__':
    unittest.main()
