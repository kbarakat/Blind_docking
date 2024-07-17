import sys
import os

path_receptor = (sys.argv[1])
receptor_pdbqt = (sys.argv[2])

with open(path_receptor) as f:
	contents = f.readlines()

tokens = str.split(contents[0],'\n')

pos = []
if tokens[0] == 'Sorry, there are no Gasteiger parameters available for atom 1T64_LOCK: :ZN 365:ZN':
	with open(receptor_pdbqt) as f:
		contents = f.readlines()
	for i in range(len(contents)):
		if contents[i][77:79] == 'Zn':
			pos.append(i)

for i in range(len(pos)):
	tokens = str.split(contents[pos[i]],' ')
	for j in range(len(tokens)):
		if tokens[j] == 'Zn\n':
			index = j
	tokens[index-1] = '2.000'
	contents[pos[i]] = ' '.join(tokens)

with open(receptor_pdbqt, 'w') as f:
	df_string = ''.join(contents)
	f.write(df_string)

