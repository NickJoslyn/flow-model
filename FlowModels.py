## Python file for solving Flow Based Models
## Function page -- call the defined function from another file

# Import list of OD pairs
# Run function on OD pairs according to Flow Model
# Return optimal locations

## Could have the optimization function an input parameter

## Could be the case we have multiple functions here that we are able to call
## FCLM, FRLM, SFCLM, . . .
#------------------------------------------------------------
import numpy as np
import pandas as pd
#------------------------------------------------------------
#Start with basic FCLM

#Basic parameters
numberOptimized = 1
totalFlow = 0
optimalLocations = np.arange(numberOptimized)

#-------------------------
# 1) Read-in files
# Don't need all of this, but could be important

#Origins - Probably a CSV
originsFile = 'OriginInformation.csv'
OriginsInformation = pd.read_csv(originsFile)
#or OriginInformation.shape[1]
numberOfOrigins = len(OriginInformation.index)
#Destinations - Probably a CSV
destinationsFile = 'DestinationInformation.csv'
DestinationsInformation = pd.read_csv(destinationsFile)

#Demand - Probably a txt file
ODFile = 'ODmatrix.txt'
ODMatrix = np.genfromtxt(ODFile)
#-------------------------

#-------------------------
# 2) Set Up Current Solution

solutionMatrix = np.ndarray(shape = (numberOfOrigins, numberOptimized))

#Don't need . . .
for i in range(numberOptimized):
    optimalLocations[i] = i

for i in range(numberOptimized):
    solutionMatrix[:,i] = ODMatrix[:,optimalLocations[i]]

flowCovered = np.sum(solutionMatrix, axis = 0)

# Currently is cannibalized . . .
for i in range(numberOptimized):
    totalFlow += flowCovered[i]
#-------------------------

#-------------------------
# 3) Vertex Substitution to check all solutions

whileCounter = 0
while(whileCounter < (numberOptimized * numberOfOrigins)):
    solutionMatrixTest = np.ndarray(shape = (numberOfOrigins, numberOptimized))
    totalFlowTest = 0
    whileCounter = 0

    for i in range(numberOptimized):
        for j in range(numberOfOrigins):
            temporaryLocations = np.copy(optimalLocations)
            temporaryLocations[i] = j

            for k in range(numberOptimized):
                solutionMatrixTest[:,k] = ODMatrix[:,temporaryLocations[k]]

            flowCoveredTest = np.sum(solutionMatrixTest, axis = 0)

            for m in range(numberOptimized):
                totalFlowTest += flowCoveredTest[m]

            if (totalFlowTest <= totalFlow):
                whileCounter += 1

            else:
                totalFlow = totalFlowTest
                optimalLocations[i] = j

            totalFlowTest = 0
            solutionMatrixTest = np.ndarray(shape = (numberOfOrigins, numberOptimized))
#-------------------------

#-------------------------
# 4) Print and check results
print("Total Flow Captured: ")
print(totalFlow)
print("Optimal Locations: ")
print(optimalLocations)

#-------------------------
