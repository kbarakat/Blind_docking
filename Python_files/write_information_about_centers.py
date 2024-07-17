import array
import fileinput
import string
import sys
import os
import math
run = 0
selected_atoms_index = 0
group = 0
selected_atoms_cut = int(sys.argv[3])
serial = ""
# serial can be used in vmd, it will accumulate the serial numbers of the surface atoms.
#serial = " "
filename_area =  (sys.argv[1]) # the area file
filename_pdb =  (sys.argv[2])  # the original receptor pdb file
surface_atom_list = []
x_of_selected_atoms = []
y_of_selected_atoms = []
z_of_selected_atoms = []
x = 0.0
y = 0.0
z = 0.0
atom_index = 0
for line in fileinput.input( filename_area ):
    line_str = line
    run = run + 1
    if (run > 1):
        if (float  (line_str[15:24]) > 0):
            #print  (line_str[0:8]) ,   (line_str[15:24])
            surface_atom_list.append( int(line_str[0:8]))
            #serial = serial +  line_str[0:8]
#print surface_atom_list
#print serial
#for i in range( len(surface_atom_list)):
 #   print i,  surface_atom_list[i]
run = 0
atom_index = 0
for line in fileinput.input( filename_pdb ):
    line_str = line
    run = run + 1
    if (line_str[0:4] == "ATOM"):
        if (int (line_str[5:12]) == (surface_atom_list[atom_index] + 1) ):
            #print int (line_str[5:12]), float(line_str[31:38]) , float(line_str[39:46]) , float(line_str[47:54])
            x_of_selected_atoms.append(float(line_str[31:38]))
            y_of_selected_atoms.append(float(line_str[39:46]))
            z_of_selected_atoms.append(float(line_str[47:54]))
            atom_index = atom_index + 1
                

#print "Total number of surface exposed atoms = " + str (len ( x_of_selected_atoms))    
#print "number of groups = " + str((len ( x_of_selected_atoms) / selected_atoms_cut + 1))

for i in range (0,len( x_of_selected_atoms)):
    #print i
    serial = serial + " " + str(surface_atom_list[i])
    selected_atoms_index = selected_atoms_index + 1
    x = x + x_of_selected_atoms [i]
    y = y + y_of_selected_atoms [i]
    z = z + z_of_selected_atoms [i]
    if (selected_atoms_index == selected_atoms_cut):
        group = group + 1
        print("group = " + str(group))
        print(serial)
        serial = ""
        selected_atoms_index = 0
        x = x / selected_atoms_cut
        y = y / selected_atoms_cut
        z = z / selected_atoms_cut
        print("center of group " + str (group))
        print(str(x)+", "+str(y)+", "+str(z))
        x = 0.0
        y = 0.0
        z = 0.0
x = 0.0
y = 0.0
z = 0.0
#serial = " "
print("group = " + str(group + 1))

for i in range ((group * selected_atoms_cut) -1 , len ( x_of_selected_atoms)  ):
    serial = serial + " " + str (surface_atom_list[i])
    x = x + x_of_selected_atoms [i]
    y = y + y_of_selected_atoms [i]
    z = z + z_of_selected_atoms [i]
x = x / (len ( x_of_selected_atoms) - ((group * selected_atoms_cut) -1))  
y = y / (len ( x_of_selected_atoms) - ((group * selected_atoms_cut) -1))
z = z / (len ( x_of_selected_atoms) - ((group * selected_atoms_cut) -1))
print(serial)
print("center of group " + str(group + 1))
serial = " "
print(str(x)+", "+str(y)+", "+str(z))
  
