# Opening input and output files
fileIn = open('chairsin.txt', 'r')
fileOut = open('chairsout.txt', 'w')

# Reading in the input file
# - C is the number of chairs
# - N is the number of friends you have
# - K is the number of friends who are willing to sit on wet chairs
# - chairs is an array of the state of each chair
C, N, K = map(int, fileIn.readline().split())
chairs = list(fileIn.readline().strip())

# Store your answer in the following variable
answer = 0

# TODO: Write your own code here



# Writing the answer to the output file
fileOut.write('%d\n' % answer)
# Done :) Closing the input and output files
fileIn.close()
fileOut.close()