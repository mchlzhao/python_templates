# Opening input and output files
fileIn = open('cavalryin.txt', 'r')
fileOut = open('cavalryout.txt', 'w')

# Reading in the input file
# - N is the number of knights
# - A is a list of the sizes of squad each knight requires
A = list(map(int, fileIn.readlines()))
N, A = A[0], A[1:]

# Store whether it is possible in the following variable
answer = True

# TODO: Write your own code here



# Writing the answer to the output file
fileOut.write('YES' if answer else 'NO')
# Done :) Closing the input and output files
fileIn.close()
fileOut.close()