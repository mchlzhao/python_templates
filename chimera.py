# AIO 2017: Chimera II
# Opening input and output files
fileIn = open('chimin.txt', 'r')
fileOut = open('chimout.txt', 'w')

# Reading in the input file
# - N is the length of the sequences
# - A and B are lists of chars, with the DNA sequences you have
# - C is a list of chars, with the DNA sequence required
N = int(fileIn.readline())
A = list(fileIn.readline().strip())
B = list(fileIn.readline().strip())
C = list(fileIn.readline().strip())

# - Store whether it is possible in the variable success
# - If it is possible, store the minimum number of splices
#   required in the variable minSplices
isSuccess = False
minSplices = 0

# TODO: Write your own code here



# Writing the answer to the output file
if isSuccess:
    fileOut.write('SUCCESS\n%d\n' % minSplices)
else:
    fileOut.write('PLAN FOILED')
# Done :) Closing the input and output files
fileIn.close()
fileOut.close()
