from team_2_sex import Sex

class Individual:
    """
        Represents an individual in a population. Has attributes
        alleles (a 2-tuple whose elements are 0, 1, or 2, indicating the individual
        has allele 0, allele 1, or allele 2) and sex (Sex.M or Sex.F)

        Young, Gibson, Jennings, and Smith
    """
    def __init__(self, alleles, sex):
        """
            Constructs an individual with a certain set of alleles and a sex
        """
        # Check the input
        for allele in alleles:
            if allele not in range(3):
                exit("Error creating individual: Allele must be either 0, 1, or 2.")
        if sex not in Sex.options:
            exit("Error creating individual: Sex must be either M or F.")

        self.alleles = tuple(alleles)
        self.sex = Sex(sex)

    def getAlleles(self):
        """
            Return: the list of alleles associated with this individual
        """
        return self.alleles

    def getSex(self): # *immature snicker*
        """
            Return: the sex of this individual
        """
        return self.sex

