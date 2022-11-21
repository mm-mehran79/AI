class CSP:
    def __init__(self, number_of_marks):
        """
        Here we initialize all the required variables for the CSP computation,
        according to the number of marks.
        """
        # Your code here
        self.number_of_marks = number_of_marks
        self.current_length = 0  # Update this line
        self.variables = []  # Update this line
        self.differences = [[]]  # Update this line

    def assign_value(self, i, v):
        """
        assign a value v to variable with index i
        """
        # Your code here
        pass

    def check_constraints(self) -> bool:
        """
        Here we loop over the differences array and update values.
        Meanwhile, we check for the validity of the constraints.
        """
        # Your code here
        pass

    def backtrack(self, i):
        """
         In this function we should loop over all the available values for
         the variable with index i, and recursively check for other variables values.
        """
        # Your code here
        pass

    def forward_check(self, i):
        """
        After assigning a value to variable i, we can make a forward check - if needed -
        to boost up the computing speed and prune our search tree.
        """
        # Your code here
        pass

    def find_minimum_length(self) -> int:
        """
        This is the main function of the class.
        First, we start by assigning an upper bound value to variable current_length.
        Then, using backtrack and forward_check functions, we decrease this value until we find
        the minimum required length.
        """
        # Your code here
        while True:
            pass
        return 0

    def get_variables(self) -> list:
        """
        Get variables array.
        """
        # No need to change
        return self.variables
