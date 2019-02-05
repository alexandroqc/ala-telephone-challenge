class OperatorsDirectory():
    def __init__(self):
        self.operators = []
    
    """
        Add an operator which is a list of prefixies and costs
    """
    def add_operator(self, operator):
        self.operators.append(operator)
    
    """
        Fill Operator function is not finished yet
    """
    def fill_operator(self, operator):
        prefixes_count = read('Number of prefixies: ')
        operator = {}
        for number in prefixes_count:
            prefix = str(read('Insert prefix: '))
            cost = read('Insert cost: ')
            operator[prefix: cost]
        operators.append(operator)

    """
        Show a table which include prefixies and costs of each operator
    """
    def show_operators(self):
        for operator in self.operators:
            print('\n PREFIX \t \t COST')
            print('=============================')
            for prefix in operator:
                print('{} \t \t {}'.format(prefix, operator[prefix]))

    """
        Search: This is a recursive function which asign a phone number to a 
        prefix and returns its cost.
        If a phone number does not match with any prefix we return cost -1
    """
    def search(self, prefix_dict, phone, cost):
        if len(phone) >= 1 or len(prefix_dict) > 0 and cost > -1:
            new_prefix_dict = {}
            for prefix in prefix_dict:
                if phone[0] == prefix[0]: # We ask if the first character of the prefix match with our phone
                    if len(prefix) > 1:
                        # Creating a new prefix_dict which is needed for the next step
                        new_prefix_dict[prefix[1:]] = prefix_dict[prefix]
                    else:
                        # If there is a only prefix matching, we will take its cost (Only answer)
                        cost = prefix_dict[prefix]
            if len(new_prefix_dict) == 1:
                key, value = new_prefix_dict.popitem()
                if len(key) > 1:
                    new_prefix_dict = {str(key): float(value)}
                    return self.search(new_prefix_dict, phone[1:], cost)
                else:
                    return value
            else:
                return self.search(new_prefix_dict, phone[1:], cost)
        else:
            return cost

    """
        This function generate a list of costs of every operator 
        and find the lowest. Return -1 if search function can not 
        find any prefix.
    """
    def low_cost(self, phone):
        costs = []
        for operator in self.operators:
            resul = self.search(operator, phone, -1)
            if resul != -1:
                costs.append(resul)
        if costs == []:
            return -1
        else:
            return min(costs)
