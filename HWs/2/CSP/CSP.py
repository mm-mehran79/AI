import numpy as np
class CSP:
    def __init__(self, number_of_marks):
        """
        Here we initialize all the required variables for the CSP computation,
        according to the number of marks.
        """
        # Your code here
        self.number_of_marks = number_of_marks
        self.current_length = 0
        self.variables = [0]  
        self.differences = []
        self.domains = [[]]

    def assign_value(self, i, v):
        """
        assign a value v to variable with index i
        """
        if len(self.variables[i]) <= i:
            self.variables.append(v)
        else :
            self.variables[i] = v

    def check_constraints(self) -> bool:
        """
        Here we loop over the differences array and update values.
        Meanwhile, we check for the validity of the constraints.
        """
        if self.variables[-1] in self.variables[:-1] : return False
        diffsNew = np.abs(np.array(self.variables[:-1]) - self.variables[-1])
        for diff in diffsNew:
            if diff in self.differences: return False
        self.differences.append(list(diffsNew))
        return True
        

    def backtrack(self, i): #return true for success and return false for failure
        """
         In this function we should loop over all the available values for
         the variable with index i, and recursively check for other variables values.
        """
        # Your code here
        if i == self.number_of_marks: return True # if assignment is complete
        self.domains.append(list(range(self.variables[-1] + 1, self.current_length + 1)))
        self.forward_check(i)
        for value in self.domains[i]:
            self.assign_value(i,value)
            if self.check_constraints:
                if self.backtrack(i + 1):
                    return True
        if self.domains[i]:
            self.variables.pop(i)
        return False

    def forward_check(self, i):
        """
        After assigning a value to variable i, we can make a forward check - if needed -
        to boost up the computing speed and prune our search tree.
        """
        for value in self.domains[i]:
            self.assign_value(i,value)
            if not self.check_constraints:
                self.domains[i].remove(value)
        if self.domains[i]:
            self.variables.pop(i)

        """
        for j in range(i - 1):
            diff = np.abs(np.array(self.domains[j]) - self.variables[i])
            for k in range(len(self.domains[j])):
                if diff[k] in self.differences or diff[k] == 0:
                    self.domains[j].remove(diff[k])
        """

    def find_minimum_length(self) -> int:
        """
        This is the main function of the class.
        First, we start by assigning an upper bound value to variable current_length.
        Then, using backtrack and forward_check functions, we decrease this value until we find
        the minimum required length.
        """
        # Your code here
        bestVariable = []
        self.current_length = self.number_of_marks *self.number_of_marks - self.number_of_marks

        while True:
            self.variables = [0]  
            self.differences = []
            self.domains = [[]]
            if self.backtrack(1) :
                self.current_length = self.variables[self.number_of_marks - 1] - 1
                bestVariable = self.variables.copy()
            else :
                self.variables = bestVariable
                break
        return bestVariable[-1]

    def get_variables(self) -> list:
        """
        Get variables array.
        """
        # No need to change
        return self.variables
