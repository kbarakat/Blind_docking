import fileinput
import sys

filename_area = (sys.argv[1])
filename_pdb = (sys.argv[2])
outfile_pdb = (sys.argv[3])
run = 0
atom_number = []

for line in fileinput.input(filename_area):
	run = run + 1
	if run > 1:
		if float(line[15:24]) > 0:
			atom_number.append(int(line[0:8]))

entry = []
run = 0
for line in fileinput.input(filename_pdb):
	if line[0:4]=="ATOM":
		for i in range(len(atom_number)):
			if atom_number[i] == int(line[4:11]):
				entry.append(line)

file = open(outfile_pdb, "w")
for i in range(len(entry)):
	file.write(entry[i])
