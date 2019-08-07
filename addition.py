# Opening input and output files
fileIn = open('addin.txt', 'r')
fileOut = open('addout.txt', 'w')

# Reading in the input file
# - A and B are the two numbers to add
A, B = map(int, fileIn.readline().split())

# Store your answer in the following variable
answer = 0

# TODO: Write your own code here



# Writing the answer to the output file
fileOut.write('%d\n' % answer)
# Done :) Closing the input and output files
fileIn.close()
fileOut.close()