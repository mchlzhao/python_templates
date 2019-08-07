# Opening the input and output files
fileIn = open('tagin.txt', 'r')
fileOut = open('tagout.txt', 'w')

# Reading in the input file
# - N is the number of players
# - M is the number of tags
# - tags is the chronological list of pairs (a, b)
#   where player a tags player b
N, M = map(int, fileIn.readline().split())
tags = []
for i in range(M):
    tags.append(list(map(int, fileIn.readline().split())))

# Store your answers in the following variables
redTeamSize = 0
blueTeamSize = 0

# TODO: Write your own code here



# Writing the answers to the output file
fileOut.write('%d %d\n' % (redTeamSize, blueTeamSize))
# Done :) Closing the input and output files
fileIn.close()
fileOut.close()