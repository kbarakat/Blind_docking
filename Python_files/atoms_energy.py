# Python file to list the atom numbers with their respective energy based on the histogram.
import os
import sys
import fileinput

aux_path1 = (sys.argv[1])
aux_path2 = (sys.argv[2])
aux_path3 = (sys.argv[3])


aux1 = []
aux2 = []
for line in fileinput.input(aux_path1):
  str_line = line
  tokens1 = str.split(str_line,'\n')
  
  tokens2 = str.split(tokens1[0],'_')

  aux1.append(tokens1[0])
  aux2.append(tokens2[3])

aux3 = []
for i in range(len(aux1)):
  histo = aux1[i]
  energy = aux2[i]
  for line in fileinput.input(aux_path2 + histo):
    str_line = line
    tokens3 = str.split(str_line,'\n')
    aux3.append(tokens3[0])

  aux4 = []
  #print(aux1)
  for line in fileinput.input(aux_path2 + aux1[i]):
    str_line = line
    tokens4 = str.split(str_line,'\n')
    aux4.append(tokens4[0])
  
  for j in range(len(aux4)):
    for line in fileinput.input(aux_path3):
      str_line = line
      tokens5 = str.split(str_line,' ')
      if aux4[j] == tokens5[0]:
        tokens6 = str.split(tokens5[1],'\n')
        tokens6 = str.split(tokens6[0],'/')
        for k in range(len(tokens6)):
          print(str(tokens6[k])+' '+str(energy))
