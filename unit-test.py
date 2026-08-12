import unittest


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Test(unittest.TestCase):
    def test(self):
        t = Triangle(10, 5)
        self.assertEqual(t.area(), 25)

    def test_zero_area(self):
        t = Triangle(0, 5)
        self.assertEqual(t.area(), 0)

    def test_negative_area(self):
        t = Triangle(-10, 5)
        self.assertEqual(t.area(), -25)

    def test_float_area(self):
        t = Triangle(10.5, 5.2)
        self.assertAlmostEqual(t.area(), 27.3, places=1)

    def test_zero_height(self):
        t = Triangle(10, 0)
        self.assertEqual(t.area(), 0)

    def test_integer(self):
        t = Triangle(10, "5")
        with self.assertRaises(TypeError):
            t.area()


unittest.main()
