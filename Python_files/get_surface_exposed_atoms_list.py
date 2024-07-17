import array
import fileinput
import string
import sys
import os
import math
run = 0
# serial can be used in vmd, it will accumulate the serial numbers of the surface atoms.
serial =  ""
filename_area = (sys.argv[1]) # the area file
surface_atom_list = []
atom_index = 0
for line in fileinput.input( filename_area ):
    line_str = line
    run = run + 1
    if (run > 1):
        if (float(line_str[15:24]) > 0):
            #print  (line_str[0:8]) ,   (line_str[15:24])
            surface_atom_list.append(int(line_str[0:8]))
            serial = serial + line_str[0:8]
print(serial)
