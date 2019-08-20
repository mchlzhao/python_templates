# Opening input and output files
fileIn = open('snakein.txt', 'r')
fileOut = open('snakeout.txt', 'w')

# Reading in the input file
# - X and Y are coordinates of the goal square
X, Y = map(int, fileIn.readline().split())

# Store your answer in the following variable
# Append the letters 'L' or 'R' representing the moves to the following list
answer = []

# TODO: Write your own code here



# Writing the answer to the output file
fileOut.write(''.join(answer))
# Done :) Closing the input and output files
fileIn.close()
fileOut.close()