import array
import fileinput
import sys
import os
# take file2 as an argument                                                     
filename =  (sys.argv[1])
pob_limit = int(sys.argv[2])
for line in fileinput.input(filename):
    if line[0:15] != 'largestCl_dlgfn':
      lin_str = line
      tokens = str.split(lin_str, ',')
      if (int(tokens[3]) > (pob_limit-1)):
        print(tokens[0] + "/" + str(int(tokens[1])) + "/" + str(int(tokens[2])) + "/" + str(int(tokens[3])) + "/"+ str(float(tokens[4])) + "/"+ str(float(tokens[5])) + "/"+ str(int(tokens[6]))+ "/"+ str(int(tokens[7]))+ "/"+ str(int(tokens[8]))+ "/"+ str(float(tokens[9])))
