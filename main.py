from telephone_operator import Operator
# phone = '4673212345'

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

# phone = '4673212345'
# phone = '87097978'
phone = '4683212345'

print(operators.low_cost(phone))