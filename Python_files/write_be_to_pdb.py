import array
import fileinput
import string
import sys
import os
pdb = (sys.argv[1])
atoms = (sys.argv[2])

pdb_file_lines = []
atom_list = []

Res_list= []
filted_res_list = []
filtered_energy_list = []
temp_line = ""
old_res = 0
new_res = 0

for line1 in fileinput.input( pdb ):
    pdb_file_lines.append(line1)
for line2 in fileinput.input( atoms ):
    aux = str.split(line2,'\n')
    atom_list.append(aux[0])

for j in range (len(atom_list)):
    tokens = str.split(atom_list[j], ' ' )
    for i in range (len(pdb_file_lines)):
        if (int(pdb_file_lines[i][5:12]) == int(tokens[0])):
            Res_list.append(int(pdb_file_lines[i][22:27]))
#print(Res_list)
#filter residue list
for j in range (len(Res_list)):
    tokens = str.split(atom_list[j], ' ' )
    old_res = int(Res_list[j])
    if (new_res != old_res):
        filted_res_list.append(old_res)
        filtered_energy_list.append(float(tokens[1]))
    new_res = old_res

for j in range (len(filted_res_list)):
    for i in range (len(pdb_file_lines)):
        if (int(pdb_file_lines[i][22:27]) == int(filted_res_list[j])):
            aux = pdb_file_lines[i][0:61]
            tokens = str.split(aux,'\n')
            print(tokens[0] + '     ' + str(float(filtered_energy_list[j])))
