"""
    This file is used to set the parameters for the genetic drift modeler.
    It's pure Python, so if you want to use some complex functions to define your
    parameters, you can.

    Young, Gibson, Jennings, and Smith
"""

# The fixed number of individuals in the population at each generation
popSize = 100

# A dictionary associating numbers of offspring produced at a time with a
# probability. (Note that these probabilities should sum to 1.)
# E.g., when a cat reproduces, it has 1 to 5 kittens with the following
# probabilities:
#       1: 10% of the time
#       2: 20% of the time
#       3: 40% of the time
#       4: 20% of the time
#       5: 10% of the time
# In this case, your dictionary would be {1: 0.1, 2: 0.2, 3: 0.4, 4: 0.2, 5: 0.1 }.
# Note that you can leave out any values that have zero probability. Thus, a sea
# turtle might have a dictionary like this:
#    { 100: 0.1, 101: 0.4, 102: 0.3, 103: 0.2 }
probOfLitterSize = { 1: 0.25, 2: 0.25, 3: 0.25, 4: 0.25 }

# The initial frequencies of the three alleles in the population
startingFrequencies = ( 0.05, 0.05, 0.9 )

# The species name (only used for debugging purposes)
name = "T. rex"

# The number of samples to collect (we will go through the simulation this
# many times)
numberOfRuns = 100

# If you want to simulate a fixed number of generations, give this a non-zero
# value. Otherwise, leave it at 0 to run until fixation/extinction.
fixedNumberOfGenerations = 0


# Settings for Florida panthers:
# popSize = ?
# probOfLitterSize = ?
# startingFrequencies = ( ? )
