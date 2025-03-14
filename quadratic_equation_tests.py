import unittest
from quadratic_equation import QuadraticEquation


class QuadraticEquationTestCase(unittest.TestCase):
    def test_raise_error_when_a_is_zero(self):
        # Arrange
        a, b, c = 0, 2, 4
        # Act & Assert
        self.assertRaises(ValueError, QuadraticEquation, a, b, c)

    def test_negative_delta(self):
        # Arrange
        a, b, c = 1, 2, 3
        # Act
        qe = QuadraticEquation(a, b, c)
        result = qe.solve()
        # Assert
        self.assertIsNone(result)

    def test_positive_delta(self):
        # Arrange
        a, b, c = 2, 5, 2
        # Act
        qe = QuadraticEquation(a, b, c)
        result = qe.solve()
        # Assert
        self.assertEqual(result, (-4.25, -5.75))

    def test_delta_equal_zero(self):
        # Arrange
        a, b, c = -1, 2, -1
        # Act
        qe = QuadraticEquation(a, b, c)
        result = qe.solve()
        # Assert
        self.assertEqual(result, 1.0)


if __name__ == '__main__':
    unittest.main()
