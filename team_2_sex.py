import random

class Sex:
    """
        Represents the sex of an individual.

        Young, Gibson, Jennings, and Smith
    """
    M = 0
    F = 1
    options = [ M, F ]

    def __init__(self, sex):
        """
            Create an object as either 'M' (male) or 'F' (female)
        """
        if sex == 'M' or sex == 'm' or sex == Sex.M:
            self.sex = Sex.M
        else:
            self.sex = Sex.F

    def __str__(self):
        if self.sex == Sex.M:
            return "Male"
        else:
            return "Female"

    def __eq__(self, other):
        if isinstance(other, int): # not an object, just M or F
            return other == self.sex
        else:
            return other.sex == self.sex

