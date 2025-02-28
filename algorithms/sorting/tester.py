# Simple sorting tester class
import random


class Tester:

    def __init__(self, num_cases = 100, element_bound = 1000):
        self.cases = []
        for _ in range(num_cases): 
            unsorted_lst = random.sample(range(1000), k = random.randint(10, 1000))
            self.cases.append((unsorted_lst, sorted(unsorted_lst)))
    
    def test(self, sort_func, func_name):
        print(f'Executing Test Cases for {func_name}...')
        for i, case in enumerate(self.cases):
            case = self.cases[i]
            print('Running Case', i+1, end='\r')
            output = sort_func(case[0])
            if output != case[1]:  # Func applied on unsorted lst == sorted lst
                print('Test failed :(\n')
                print('Input:\n', case[0], '\n')
                print('Output:\n', output, '\n')
                print('Expected Output:\n', case[1])
                return
            print(f'Case {i+1} passed!', end='\r')
        print('\nAll Tests passed :)')