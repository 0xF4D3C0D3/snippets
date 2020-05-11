import itertools

class CryptArithmeticSolver:
    """CryptArithmeticSolver solves cryptarithmetic problems.
(Also called alphametics or Verbal arithmetic)
    
    To use:
    >>> cas = CryptArithmeticSolver()
    >>> cas.set_problem('''
     A
     A
    CB
    ''')
    >>> g = cas.gen_solve()
    >>> next(g)
    {'C': '1', 'B': '0', 'A': '5'}
    >>> next(g)
    {'C': '1', 'B': '2', 'A': '6'}
    
    Note:
      This solver can only addition yet
    """
    
    def set_problem(self, problem: str):
        self._problem = problem
        
        # a constraint to check all the leftmost digit characters are not zero
        self.__zero_constraint = '*'.join(
            set([x.strip()[0] for x in problem.strip().splitlines()])
        ) + '!=0'
    
    def gen_solve(self):
        """returns a generator to solve current problem
        
        Returns (generator): a generator that yields a substitute table whose
          value is the answer and each character is key.
        """
        
        self._get_matrix()  # convert _problem as character matrix to create constraints easily
        self._get_constraints()  # get constraints that verifies whether the substitute satisfies the problem
        
        def gen():
            # start worker with all possible numbers, empty substitute table and the level for tracking depth
            for solution in self.__worker(bag={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
                                     tab={},
                                     level=0):
                # extract terms for last check
                terms = self._problem.translate(str.maketrans(solution)).split()
                if eval('+'.join(terms[:-1]) + '==' + terms[-1]): 
                    yield solution

        return gen()

    def print_problem(self):
        print(self._problem)
    
    def print_all_solutions(self):
        for solution in self.gen_solve():
            print(self._problem.translate(str.maketrans(solution)))
            
    def __worker(self, bag: set, tab: dict, level: int) -> dict:
        """find solutions recursively and lazily
        
        Args:
          bag (set): a possible set for remain numbers
          tab (dict): a substitute table for the answer
          level (int): a value for tracking depth
        
        Returns (dict): a substitute table satisfies the problem
        """
        
        # base case
        if level == self.__len_matrix:
            # check all the leftmost digit characters are not zero 
            if eval(self.__zero_constraint.translate(str.maketrans(tab))):
                yield tab  # if it passes yield the substitute table
            return
        
        # get possible characters to try from _matrix at the level
        # except for '0' and already tried characters
        possible_char_list = set(self._matrix[level]) - ({'0'} | tab.keys())
        
        # get next possible set by excepting already tried numbers
        next_bag = bag - set(tab.values())
        
        # travers all permutations from next_bag
        for permutation in itertools.permutations(next_bag, len(possible_char_list)):
            
            # upsert tab with new pairs to try
            next_tab = {**{c:v for c, v in zip(possible_char_list, permutation)}, **tab}
            
            # check all available constraints
            # at a level, we can check constraints till at the level
            for constraint in self._constraints[:level+1]:
                
                # if the evaluation of the substitute table is False,
                # then break and not step into else block
                if eval(constraint.translate(str.maketrans(next_tab))) is False:
                    break
            else:
                # when all constraints are passed, yield it and continue
                for solutions in self.__worker(next_bag, next_tab, level+1):
                    yield solutions
        
    def _get_matrix(self):
        """ get the character matrix from the problem string
 AB
 CD  -> [('B', 'D', 'G'), ('A', 'C', 'F'), ('0', '0', 'E')]
EFG
        """
        
        lines = self._problem.strip().splitlines()
        max_len = max(map(len, lines))  # get max length for padding
        
        # get zero-padded and uppercased terms
        pads = [f'{x.strip():0>{max_len}}'.upper() for x in lines]
        
        # transpose and reverse the terms to verify from the rightmost digit
        self._matrix = list(itertools.zip_longest(*pads))[::-1]
        self.__len_matrix = len(self._matrix)

    def _get_constraints(self):
        """get constraints that verifies whether the substitute satisfies the problem
 AB       ['G == (B+D)%10',
 CD   ->   'F == ((B+D)//10+A+C)%10',
EFG        'E == (((B+D)//10+A+C)//10+0+0)%10']
        """
        
        constraint_list = []
        prev = None  # for the previous digit
        for matrix in self._matrix:
            if prev is None:  # if this digit is the rightmost then no carry on it
                prev = '+'.join(matrix[:-1])
            else:  # if this isn't rightmost digit then there may be a carry
                prev = f"({prev})//10+{'+'.join(matrix[:-1])}"
            constraint_list += [f"{matrix[-1]} == ({prev})%10"]

        self._constraints = constraint_list
        
if __name__ == '__main__':
    cryptArithmeticSolver = CryptArithmeticSolver()
    cryptArithmeticSolver.set_problem('''
      OHIO
      IOWA
      UTAH
     MAINE
    HAWAII
    ''')

    cryptArithmeticSolver.print_problem()
    print('  ▼  ▼  ▼  ▼  ▼')
    cryptArithmeticSolver.print_all_solutions()
