"""
    Program to simulate genetic drift of three alleles in a constant-size population.

    Young, Gibson, Jennings, and Smith

    Written for Python 3
"""

from team_2_species import Species
from team_2_simulator import *
from team_2_settings import *
import math
import os


def generationsToFixation(freqsOverTime):
    """
        Return: the first generation in which an allele became fixed in the
                frequency-over-time data
    """
    for i in range(len(freqsOverTime)):
        if 1.0 in freqsOverTime[i]:
            return i
    return -1

def standardDev( listOfValues ):
    """
        Return: the standard deviation of the list of values
                Note: sd(. . .) = sqrt( \sum_i( x_i - mean )^2 / n - 1 )
                Note: this function discards values of -1 (which in our case
                      indicates a dummy value)
    """
    mean = sum(listOfValues)/len(listOfValues)
    sd = 0.0
    for x in listOfValues:
        if x != -1:
            sd += (x - mean)**2
    sd = math.sqrt(sd)/(len(listOfValues) - 1)
    return sd

def countFixationsByAllele( allRuns, listOfFixationGenerations ):
    """
        Counts the number of times each allele was fixed.
        Params:
            allRuns: The frequency data for all sample simulations
            listOfFixationGenerations: The list indicating in which generation a
                                       fixation occurred, as returned by
                                       generationsToFixation()
        Returns: a 3-tuple, which is:
                   ( number of times allele 0 was fixed,
                     times allele 1 was fixed,
                     times allele 2 was fixed )
    """
    numFixations = [0.0] * 3
    for i in range(len(allRuns)):
        if listOfFixationGenerations[i] != -1: # if a fixation actually occurred here
            freqsOverTime = allRuns[i]
            thisRunsFixation = list(freqsOverTime[ listOfFixationGenerations[i] ])
            numFixations = list( x + y for x,y in zip(numFixations, thisRunsFixation) )
    return numFixations


def printStatistics( allSimulations, outputDir ):
    """
        Outputs (both to the standard out and to a text file in the output directory)
        a number of statistics on the full run of simulations.

        Parameters:
            allRuns: The allele frequency data on all simulations
            outputDir: The directory in which we should write our files
        Also uses:
            global (from settings) numberOfRuns
            global (from settings) popSize
            global (from settings) fixedNumberOfGenerations
    """
    print("              Data on the fixation events            ")
    print("-----------------------------------------------------")
    print("Sample size (number of simulations): " + str(numberOfRuns))
    print("Population size: " + str(popSize))
    print("Fixed number of generations: " + str(fixedNumberOfGenerations))

    timeToFixation = list(map(generationsToFixation, allSimulations))

    # Calculate the fixation percentage
    numFixations = sum( 1 for x in timeToFixation if x != -1 )
    if fixedNumberOfGenerations <= 0:
        percentFixations = 100
    else:
        percentFixations = (numFixations / len(allSimulations)) * 100
    print("A fixation event occurred ", percentFixations, "% of the time.")

    # Calculate the mean
    # If we used a fixed number of generations, the mean is easy
    if fixedNumberOfGenerations <= 0:
        meanTimeToFixation = sum(timeToFixation) / len(allSimulations)
    else: # Need to discard times we didn't have fixation
        meanTimeToFixation = sum(x for x in timeToFixation if x != -1) / numFixations
    print( "Mean generations to fixation: ", meanTimeToFixation )

    # Calculate the standard deviation
    sd = standardDev(timeToFixation)
    print( "Standard deviation: ", sd )

    # Calculate the min and max generations to fixation
    print( "Max generations to fixation: ", max(timeToFixation) )
    print( "Min generations to fixation: ", min(timeToFixation) )

    # Print data on how often each allele became fixed
    print("\nStarting frequencies: " + str(startingFrequencies))
    print( "Number of times each allele became fixed (a_0, a_1, a_2): ",
           countFixationsByAllele(allSimulations, timeToFixation) )

    # Write all of the above to a file for future reference
    if not os.path.exists( outputDir ):
        os.makedirs(outputDir)
    outputFile = open( outDir + "/statistics.txt",
                       "w" )
    outputFile.write("              Data on the fixation events            \n")
    outputFile.write("-----------------------------------------------------\n")
    outputFile.write("Sample size (number of simulations): "
                     + str(numberOfRuns) + "\n")
    outputFile.write("Population size: " + str(popSize) + "\n")
    outputFile.write("Fixed number of generations: " + str(fixedNumberOfGenerations)
                     + "\n")
    outputFile.write( "A fixation event occurred " + str(percentFixations)
                      + "% of the time.\n" )
    outputFile.write( "Mean generations to fixation: " + str(meanTimeToFixation)
                      + "\n" )
    outputFile.write( "Standard deviation: " + str(sd) + "\n" )
    outputFile.write( "Max generations to fixation: " + str(max(timeToFixation))
                      + "\n" )
    outputFile.write( "Min generations to fixation: " + str(min(timeToFixation))
                      + "\n" )
    outputFile.write("\nStarting frequencies: " + str(startingFrequencies) + "\n")
    outputFile.write( "Number of times each allele became fixed (a_0, a_1, a_2): "
                      + str(countFixationsByAllele(allSimulations, timeToFixation))
                      + "\n" )
    outputFile.close()








##                               Main program                                      ##
#####################################################################################

# Create the output directory if necessary
outDir = "output"
if not os.path.exists( outDir ):
    os.makedirs(outDir)

allRuns = []
# For each simulation, write the data to a file in the output directory
for repetition in range(numberOfRuns):
    theSpecies = Species( popSize, startingFrequencies, probOfLitterSize, name )
    freqsOverTime = simulateDrift( theSpecies,
                                   bool(fixedNumberOfGenerations > 0),
                                   fixedNumberOfGenerations )
    allRuns.append(freqsOverTime)

    outputFile = open( outDir + "/frequency_over_time" + str(repetition) + ".tsv",
                       "w" )
    # Write the header
    outputFile.write("#Generation\tAllele0 Freq\tAllele1 Freq\tAllele2 Freq\n")

    # Write the actual data
    for generation in range(len(freqsOverTime)):
        outputFile.write( str(generation) + "\t" )
        outputFile.write( '\t'.join( format( freq, "1.4f")
                                     for freq in freqsOverTime[generation] ) )
        outputFile.write( "\n" )

    outputFile.close()

# Output statistics about our simulations
printStatistics( allRuns, outDir )
