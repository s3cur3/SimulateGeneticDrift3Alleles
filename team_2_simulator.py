from team_2_species import Species
from team_2_sex import Sex
from team_2_individual import Individual
import random, math

def simulateDrift( species, endAfterFixedNumGenerations=False, numGenerations=0 ):
    """
       Simulates genetic drift of three alleles in a given species.

       Parameters:
           species: An object of the Species class, representing a particular
                    population of a given species undergoing genetic drift on 3
                    alleles.
           endAfterFixedNumGenerations: If true, the simulation will run for a
                                predetermined
                                number of generations. If false, the simulation will
                                continue until one allele has become fixed.
           generation: the current generation


       Returns: a list of 3-tuples. The 3-tuple at position i represents the
                frequencies of the three alleles at generation i of the simulation.
                (Note that this means position 0 contains the starting frequencies.)
    """

    def finished( frequencies, generation, endAfterFixedNumGenerations ):
        """
           Private to simulateDrift().

           Checks to see if the simulation is finished. Requires:
               frequencies: The 3-tuple of frequencies for the previous generation
               currentGen: This generation's number

           Uses: endAfterFixedNumGenerations

           Return: true if the simulation is finished, false otherwise.
        """
        # If we're supposed to go a fixed number of generations, check to see
        # if we've gone that far
        if endAfterFixedNumGenerations:
            return bool(generation >= numGenerations)
        # Otherwise, we're supposed to go until fixation
        else:
            return bool(1.0 in frequencies)

    def simulateSingleGeneration( species ):
        """
           Private to simulateDrift().

           Simulates genetic drift for a single generation. This is where all
           the magic happens.

           The simulation runs as follows:
           - Begin with a parent population, separated into males and females
           - Randomly select two individuals to reproduce. If
           - Continue selecting individuals to reproduce until we have
             [population size] new individuals in this generation
           - Calculate and return the allele frequencies in the new generation

           Parameter species: The object representing the relevant population of our
                              species. This will be updated with the new population.

           Returns: A 3-tuple of the new frequencies for the next generation.
        """

        def randomNumOffspring( probabilityDictionary ):
            """
                Private to simulateSingleGeneration().

                Returns an integer, which is the randomly chosen number of offspring
                in this "litter."
                Param probabilityDictionary: a dictionary whose keys are numbers of
                            offspring per litter and values are probabilities. See
                            documentation in the Species constructor for more info.
                Return: the randomly chosen number of offspring in this "litter."
            """
            while True: # loop until we return
                # Select a key to "roll the dice" for; if we generate a probability
                # matching this number's associated probability, we return that
                # number
                keyToRollFor = random.choice( list(probabilityDictionary.keys()) )
                r = random.uniform(0, 1)
                if r < probabilityDictionary[keyToRollFor]:
                    return keyToRollFor



        size = species.getPopulationSize()

        parentPop = species.getPopulation()
        random.shuffle(parentPop) # randomize the population; this is important!!

        # Separate the parents by sex
        def isMale(x): return x.getSex() == Sex.M
        daddies = list( filter( isMale, parentPop ) )
        def isFemale(x): return not isMale(x)
        mommies = list( filter( isFemale, parentPop ) )

        childPopulation = []
        while len(childPopulation) < size:
            # Create a "child" with one allele from two parents
            dad = random.choice(daddies)
            mom = random.choice(mommies)

            totalOffspring = \
                randomNumOffspring( species.getProbOfProducingNumOffspring() )
            for offspring in range(totalOffspring):
                childAlleles = [ random.choice(dad.getAlleles()),
                                 random.choice(mom.getAlleles()) ]
                # Shuffle so that allele0 doesn't always come from dad
                random.shuffle( childAlleles )

                child = Individual( tuple(childAlleles), random.choice(Sex.options))
                childPopulation.append( child )

        # Because the number of offspring produced may be greater than the fixed
        # population size (due to the fact that parents can have more than one child
        # at a time), we'll randomly bring the population size back to the desired
        # value
        while len(childPopulation) > size:
            del childPopulation[ random.choice(range(len(childPopulation))) ]

        species.setPopulation( childPopulation )





    # Sanity-check the input
    if (not endAfterFixedNumGenerations) and numGenerations != 0:
        exit("Sorry, you can't request that we simulate drift until fixation while "
             + "also running a fixed number of generations.")
    elif endAfterFixedNumGenerations and numGenerations < 0:
        exit("Sorry, number of generations to simulate must be positive.")

    if math.fsum(species.getAlleleFrequencies()) != 1.0:
        exit( "Sorry, starting allele frequencies must sum to 1 "\
              + "(yours sum to " + str(sum(species.getAlleleFrequencies())) + ")." )

    if math.fsum(species.getProbOfProducingNumOffspring().values()) != 1.0:
        exit( "Sorry, probabilities of producing offspring must sum to 1 "\
              + "(yours sum to "\
              + str( math.fsum(species.getProbOfProducingNumOffspring().values()) )\
              + ")." )

    if( len(species.getAlleleFrequencies()) != 3 ):
        exit("Sorry, we require exactly 3 alleles in the population.")



    # Store the initial frequencies
    currentGen = 0
    results = []
    results.append( species.getAlleleFrequencies() )

    # Until our (complex) exit condition is satisfied, simulate a single generation
    while( not finished( species.getAlleleFrequencies(),
                         currentGen, endAfterFixedNumGenerations ) ):
        # Perform a simulation of a single generation, and update the species
        # object accordingly
        simulateSingleGeneration( species )

        # Remember these frequencies
        results.append( species.getAlleleFrequencies() )

        # Increment the counter
        currentGen += 1

    return results
