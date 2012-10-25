import random, math
from team_2_individual import Individual
from team_2_sex import Sex

class Species:
    """
        Young, Gibson, Jennings, and Smith

        A class to represent a particular species. Stores information about
        the population size, the frequencies of the three alleles, and
        each member's probability of producing a given number of offspring.

        Written for Python 3
    """

    def __init__(self, populationSize, startingFrequencies,
                 probOfOffspringInLitter, name="species"):
        """
           The constructor for the species. Requires:
               populationSize: the number of individuals in the population
               startingFrequencies: a 3-tuple representing the frequencies of
                                    each of the three alleles
               probOfOffspringInLitter: a dictionary containing probabilities that
                        a mother individual will produce some number of offspring,
                        where the key is the number of offspring and the value is
                        the probability. E.g., the dictionary
                                    { 1: 0.5, 2: 0.25, 3: 0.25 }
                        indicates an individual has a 50% chance of having
                        1 child at a time, a 25% chance of having 2 at a time,
                        and a 25% chance of having 3 at a time.
           Optional:
               name: The name of this species (only used when creating a string
                     representation)
        """
        self.popSize = populationSize
        self.freqs = startingFrequencies
        self.pOffspring = probOfOffspringInLitter
        self.name = str(name)



        # Set up the initial population
        allelesInPop = 2*self.popSize # diploids; 2 alleles per individual
        # Python sweetness: "[0]*n" creates a list of n instances of 0
        remainingAlleles = [0] * int(round(allelesInPop*self.freqs[0]))
        remainingAlleles.extend( [1] * int(round(allelesInPop*self.freqs[1])) )
        remainingAlleles.extend( [2] * int(round(allelesInPop*self.freqs[2])) )
        random.shuffle(remainingAlleles) # randomize the alleles

        population = [] # The population is a list of Individuals
        for individual in range(self.popSize):
            alleles = ( remainingAlleles.pop(),  # since the list was randomized,
                        remainingAlleles.pop() ) # this gives 2 random alleles
            sex = random.choice( Sex.options )
            population.append( Individual(alleles, sex) )

        self.setPopulation(population)


        
    def __str__(self):
        """
            Return: a string representation of this species population
        """
        return "Species '" + self.getName() + "' has " \
            + self.getPopulationSize() + " individuals and allele frequencies of " \
            + self.getAlleleFrequencies() + " \n"


    def getAlleleFrequencies(self):
        """
            Return: a 3-tuple representing the frequencies of each of the three
                    alleles
        """
        return tuple(self.freqs)


    def setAlleleFrequencies( self, newFrequencies ):
        """
            Param newFrequencies: a 3-tuple representing the frequencies of
                                  each of the three alleles
        """
        self.freqs = newFrequencies
        

    def getProbOfProducingNumOffspring(self):
        """
            Return: a dictionary containing probabilities that
                    a mother individual will produce some number of offspring,
                    where the key is the number of offspring and the value is
                    the probability. E.g., the dictionary
                                { 1: 0.5, 2: 0.25, 3: 0.25 }
                    indicates an individual has a 50% chance of having
                    1 child at a time, a 25% chance of having 2 at a time,
                    and a 25% chance of having 3 at a time.
        """
        return self.pOffspring

    def getPopulation(self):
        """
            Return: a list of whose elements are either 0, 1, or 2
                    (indicating that the individual represented by that number
                    carried allele 0, 1, or 2)
        """
        return self.pop

    def setPopulation(self, newPopulation):
        """
            Modifies the species' population, and automatically resets the allele
            frequencies.

            Param newPopulation: a list whose elements are Individuals
        """

        def getNewFreqs(newPop):
            """
                Calculates the allele frequencies in the new population
                Return: the list of allele frequencies
            """
            # Count the alleles
            numAlleles = [0] * 3
            for individual in newPopulation:
                for allele in individual.getAlleles():
                    # Sanity check!
                    if allele not in range(3):
                        exit("Sorry, individuals can have only alleles 0, 1, or 2.")
                    numAlleles[int(allele)] += 1

            totalAlleles = sum(numAlleles)
            return [ numAlleles[0]/totalAlleles,
                     numAlleles[1]/totalAlleles,
                     numAlleles[2]/totalAlleles ]


        # Sanity check the input
        if len(newPopulation) != self.popSize:
            exit( "Sorry, new population must have exactly " + str(self.popSize) \
                  + " individuals. This population has " + str(len(newPopulation)) \
                  + "." )

        self.pop = newPopulation
        self.setAlleleFrequencies( getNewFreqs( newPopulation ) )


    def getName(self):
        """
            Return: the name associated with this species
        """
        return str(self.name)

    def getPopulationSize(self):
        """
            Return: the (fixed) population size for this species
        """
        return self.popSize

    def countThisGenerationsHeterozygotes(self):
        """
            Counts (and remembers for future use) the number of individuals that
            are heterozygotes, homozygous for allele 0, homozygous for allele 1,
            and homozygous for allele 2.
        """
        self.numHeterozygotes = 0
        self.numHomozygotesA0 = 0
        self.numHomozygotesA1 = 0
        self.numHomozygotesA2 = 0
        for individual in self.pop:
            if individual.alleles == (0,0):
                self.numHomozygotesA0 += 1
            elif individual.alleles == (1,1):
                self.numHomozygotesA1 += 1
            elif individual.alleles == (2,2):
                self.numHomozygotesA2 += 1
            else:
                self.numHeterozygotes += 1


