import unittest
from telephone_operator import Operator

class TestLowCostMethods(unittest.TestCase):

  
    def test_default(self):
        map1 = {
            '1': 0.9,
            '268': 5.1,
            '46': 0.17,
            '4620': 0.0,
            '468': 0.15,
            '4631': 0.15,
            '4673': 0.9,
            '467320': 1.1
        }
        map2 = {
            '1': 0.92,
            '44': 0.5,
            '46': 0.2,
            '467': 1.0,
            '48': 1.2
        }
        operators = Operator()
        operators.add_operator(map1)
        operators.add_operator(map2)
        self.assertEqual(operators.low_cost('4673212345'), 1.0)


    def test_uniq_value(self):
        map1 = {
            '1': 0.9,
            '268': 5.1,
            '46': 0.17,
            '4620': 0.0,
            '468': 0.15,
            '4631': 0.15,
            '4673': 0.9,
            '467320': 1.1
        }
        map2 = {
            '1': 0.92,
            '44': 0.5,
            '46': 0.2,
            '467': 1.0,
            '48': 1.2,
            '268': 3.2
        }
        operators = Operator()
        operators.add_operator(map1)
        operators.add_operator(map2)
        self.assertEqual(operators.low_cost('26834934'), 3.2)


    def test_no_exist(self):
        map1 = {
            '1': 0.9,
            '268': 5.1,
            '46': 0.17,
            '4620': 0.0,
            '468': 0.15,
            '4631': 0.15,
            '4673': 0.9,
            '467320': 1.1
        }
        operators = Operator()
        operators.add_operator(map1)
        self.assertEqual(operators.low_cost('9348383434'), -1)


    def test_no_exist2(self):
        map1 = {
            '1': 0.9,
            '268': 5.1,
            '46': 0.17,
            '4620': 0.0,
            '468': 0.15,
            '4631': 0.15,
            '4673': 0.9,
            '467320': 1.1
        }
        map2 = {
            '1': 0.92,
            '44': 0.5,
            '46': 0.2,
            '93': 0.1,
            '48': 1.2,
            '268': 3.2
        }
        operators = Operator()
        operators.add_operator(map1)
        operators.add_operator(map2)
        self.assertEqual(operators.low_cost('9348383434'), 0.1)


    def test_default2(self):
        map1 = {
            '1': 0.9,
            '268': 5.1,
            '46': 0.17,
            '4620': 0.0,
            '468': 0.15,
            '4631': 0.15,
            '4673': 0.9,
            '467320': 1.1
        }
        map2 = {
            '1': 0.92,
            '44': 0.5,
            '46': 0.2,
            '467': 1.0,
            '48': 1.2
        }
        operators = Operator()
        operators.add_operator(map1)
        operators.add_operator(map2)
        self.assertEqual(operators.low_cost('4683212345'), 0.15)


    def test_default3(self):
        map1 = {
            '1': 0.9,
            '268': 5.1,
            '46': 0.17,
            '4620': 0.0,
            '468': 0.15,
            '4631': 0.15,
            '4673': 0.9,
            '467320': 1.1
        }
        map2 = {
            '1': 0.92,
            '44': 0.5,
            '46': 0.2,
            '467': 1.0,
            '48': 1.2
        }
        operators = Operator()
        operators.add_operator(map1)
        operators.add_operator(map2)
        self.assertEqual(operators.low_cost('234567890'), -1)

if __name__ == '__main__':
    unittest.main()