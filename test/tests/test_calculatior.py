from unittest import TestCase, main

from root_files.calculator import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('3-1'), 2)

    def test_multy(self):
        self.assertEqual(calculator('4*4'), 16)

    def test_division(self):
        self.assertEqual(calculator('4/4'), 1)

    def test_no_sign(self):
        with self.assertRaises(ValueError) as i:
            calculator('test value')
        self.assertEqual('Expression should be contain some one sign +-/*', i.exception.args[0])

    def test_two_sign(self):
        with self.assertRaises(ValueError) as i:
            calculator('10+20+2')
        self.assertEqual('Expression should be contain 2 int numbers and one sign', i.exception.args[0])

if __name__ == '__main__':
    main()
