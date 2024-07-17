import sys
import os

path_gpf = (sys.argv[1])
nx = (sys.argv[2])
ny = (sys.argv[3])
nz = (sys.argv[4])
space = (sys.argv[5])
box_name = (sys.argv[6])

with open(path_gpf) as f:
	contents = f.readlines()

for i in range(len(contents)):
	if contents[i][0:4] == 'npts':
		tokens = str.split(contents[i],' ')

		tokens[1] = nx
		tokens[2] = ny
		tokens[3] = nz

		contents[i] = ' '.join(tokens)

	if contents[i][0:7] == 'spacing':
		tokens=str.split(contents[i],' ')

		tokens[1] = space

		contents[i] = ' '.join(tokens)

	if contents[i][0:10] == 'gridcenter':
		tokens = str.split(contents[i],' ')

		aux_name = str.split(box_name,'_')

		tokens[1] = aux_name[0]
		tokens[2] = aux_name[1]
		tokens[3] = aux_name[2]

		contents[i] = ' '.join(tokens)

with open(path_gpf, 'w') as f:
	df_string = ''.join(contents)
	f.write(df_string)
