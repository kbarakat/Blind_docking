import array
import fileinput
import string
import sys
import os
# reads centers_info.txt and append the centers with the atoms
filename1 = (sys.argv[1])
count  = 0
s = ""
z = " "
for line1 in fileinput.input( filename1 ):
    count = count + 1
    if (count == 2):
        #print "count = " + str (count)
        tokens = str.split(line1, ' ')
        #print tokens
        for i in range (len( tokens)-1):
            #print i
            z = z + "/" + str((tokens[i+1]))  
        #print s
    if (count == 4):
        #print "count = " + str (count)
        tokens1 = str.split( line1, '\n' )
        tokens2 = str.split(tokens1[0],',')
        for i in range (len(tokens2)):
            s = s + str(round(float(tokens2[i]),3)) + "/"     
            #print float (tokens[i])
        print(s[:-1] + " " + z[2:])
        s = ""
        z = " "
        count = 0
