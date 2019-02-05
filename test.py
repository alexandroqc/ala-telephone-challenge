import unittest
from telephone_operator import OperatorsDirectory


class TestLowCostMethods(unittest.TestCase):

    """
        Default test taken from the pdf document.
    """
    def test_default(self):
        directory1 = {
            '1': 0.9,
            '268': 5.1,
            '46': 0.17,
            '4620': 0.0,
            '468': 0.15,
            '4631': 0.15,
            '4673': 0.9,
            '467320': 1.1
        }
        directory2 = {
            '1': 0.92,
            '44': 0.5,
            '46': 0.2,
            '467': 1.0,
            '48': 1.2
        }
        operators = OperatorsDirectory()
        operators.add_operator(directory1)
        operators.add_operator(directory2)
        self.assertEqual(operators.low_cost('4673212345'), 1.0)

    """
        This validates if there is an only posible prefix.
    """
    def test_uniq_value(self):
        directory1 = {
            '1': 0.9,
            '268': 5.1,
            '46': 0.17,
            '4620': 0.0,
            '468': 0.15,
            '4631': 0.15,
            '4673': 0.9,
            '467320': 1.1
        }
        directory2 = {
            '1': 0.92,
            '44': 0.5,
            '46': 0.2,
            '467': 1.0,
            '48': 1.2,
            '268': 3.2
        }
        operators = OperatorsDirectory()
        operators.add_operator(directory1)
        operators.add_operator(directory2)
        self.assertEqual(operators.low_cost('26834934'), 3.2)

    """
        This function validates if a phone does not match with any prefix
    """
    def test_no_exist(self):
        directory1 = {
            '1': 0.9,
            '268': 5.1,
            '46': 0.17,
            '4620': 0.0,
            '468': 0.15,
            '4631': 0.15,
            '4673': 0.9,
            '467320': 1.1
        }
        operators = OperatorsDirectory()
        operators.add_operator(directory1)
        self.assertEqual(operators.low_cost('9348383434'), -1)

    def test_no_exist2(self):
        directory1 = {
            '1': 0.9,
            '268': 5.1,
            '46': 0.17,
            '4620': 0.0,
            '468': 0.15,
            '4631': 0.15,
            '4673': 0.9,
            '467320': 1.1
        }
        directory2 = {
            '1': 0.92,
            '44': 0.5,
            '46': 0.2,
            '93': 0.1,
            '48': 1.2,
            '268': 3.2
        }
        operators = OperatorsDirectory()
        operators.add_operator(directory1)
        operators.add_operator(directory2)
        self.assertEqual(operators.low_cost('9348383434'), 0.1)

    """
        These functions evaluate if a phone does match with part of a prefix
    """
    def test_default2(self):
        directory1 = {
            '1': 0.9,
            '268': 5.1,
            '46': 0.17,
            '4620': 0.0,
            '468': 0.15,
            '4631': 0.15,
            '4673': 0.9,
            '467320': 1.1
        }
        directory2 = {
            '1': 0.92,
            '44': 0.5,
            '46': 0.2,
            '467': 1.0,
            '48': 1.2
        }
        operators = OperatorsDirectory()
        operators.add_operator(directory1)
        operators.add_operator(directory2)
        self.assertEqual(operators.low_cost('4683212345'), 0.15)

    def test_default3(self):
        directory1 = {
            '1': 0.9,
            '268': 5.1,
            '46': 0.17,
            '4620': 0.0,
            '468': 0.15,
            '4631': 0.15,
            '4673': 0.9,
            '467320': 1.1
        }
        directory2 = {
            '1': 0.92,
            '44': 0.5,
            '46': 0.2,
            '467': 1.0,
            '48': 1.2
        }
        operators = OperatorsDirectory()
        operators.add_operator(directory1)
        operators.add_operator(directory2)
        self.assertEqual(operators.low_cost('234567890'), -1)

if __name__ == '__main__':
    unittest.main()
