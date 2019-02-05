
class Operator():
  def __init__(self):
    self.operators = []

  def add_operator(self, operator):
    self.operators.append(operator)

  def fill_operator(self, operator):
    prefixes_count = read('Number of prefixes: ')
    operator = {}
    for number in prefixes_count:
      prefix = str(read('Insert prefix: '))
      cost = read('Insert cost: ')
      operator[prefix: cost]
    operators.append(operator)

  def show_operators(self):
    print(operators)

  def search(self, map, phone, cost, large):
    # print("======================================")
    # print("Count: {}".format(len(map)))
    if len(phone) >=1 or len(map) > 0 and cost > -1:
      # print("executing... "+phone[0]);
      newmap = {}
      for x in map:
        if phone[0] == x[0]:
          # print("equal: "+ x)
          if len(x)!=1:
            newmap[x[1:]] = map[x]
          else:
            print('Costo',map[x])
            cost = map[x]
      if len(newmap) == 1:
        # print(newmap)
        key, value = newmap.popitem()
        return value
      else:
        print(phone[1:]);
        return self.search(newmap, phone[1:], cost, large)
    else:
      return cost


  def low_cost(self, phone):
    costs = []
    for operator in self.operators:
      resul = self.search(operator, phone, -1, len(phone))
      if resul != -1:
        costs.append(resul)
        print('##########################################')
    if costs == []:
      return -1
    else:
      return min(costs)