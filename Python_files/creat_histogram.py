import array
import fileinput
import string
import sys
import os
import numpy as np

filename1 =  (sys.argv[1]) # summary file for that hit as generated by the main script: color_pdb_with_be.csh
energy_step  = int(sys.argv[2])
pop_limit = int(sys.argv[3])
count = 0

bins = np.arange(-10,0,energy_step)
 
for i in range(len(bins)):
  energy_step1 = bins[i]
  energy_step2 = bins[i] + energy_step
  outfile = "histogram___" + str(energy_step2)
  file = open(outfile, 'w')
  
  for line1 in fileinput.input(filename1):
    tokens = str.split(line1, ',')
    if int(tokens[3]) > (pop_limit - 1):
      if energy_step1 < float(tokens[4]) <= energy_step2:
        string1 = tokens[0]
        tokens1 = str.split(string1,'/')

        string2 = tokens1[4]
        tokens2 = str.split(string2,'_')

        s = tokens2[1]+'/'+tokens2[2]+'/'+tokens2[3]

        count = count + 1

        file.write(s+'\n')
        s = ''
  print(energy_step2,count)
  file.close()
  count = 0
