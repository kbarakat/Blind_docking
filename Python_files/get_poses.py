import sys
import os
import fileinput
import shutil

set_x = 1
set_y = 1
set_z = 0

path = (sys.argv[1])
ligand_name = (sys.argv[2])

list_box = os.listdir(path)
aux1 = str.split(path,'/dock_here')
ROOT = aux1[0]
os.mkdir(ROOT+'/Binding_modes')
os.mkdir(ROOT+'/Binding_modes/Only_the_best_dock')

for i in range(len(list_box)):
  os.mkdir(ROOT+'/Binding_modes'+'/Rank_'+str(set_x)+'_population_for_'+list_box[i])
  os.chdir(ROOT+'/Binding_modes'+'/Rank_'+str(set_x)+'_population_for_'+list_box[i])
  dlg_file = ROOT+'/dock_here/'+list_box[i]+'/'+ligand_name+'.dlg'

  run = 0.0
  x = 1000000000.0
  y = 1000000000.0
  z = 1000000000.0
  rank_of_largest_cluster = 0

  for line in fileinput.input(dlg_file):
    run = run + 1
    if (line[4:24] == "CLUSTERING HISTOGRAM"):
      #print "Start reading the Clustering Table"
      x = run # line where the string 'CLUSTERING HISTOGRAM' is located
    if (line[4:14] == "RMSD TABLE"):
      y = run
    if (line[0:8] == "Run time"):
      z = run

  path7 = ROOT+'/Binding_modes/Rank_'+str(set_x)+'_population_for_'+list_box[i]+ '/pop_list.txt'

  with open(path7, 'w') as f:
    run = 0
    list_cluster = []
    list_energy = []
    list_rank = []
    for line in fileinput.input(dlg_file):
      run = run + 1
      if (run >= x+10) and (run < y-3):
        cluster_table_entry =  line[0:42]
        tokens = str.split(cluster_table_entry, '|' )
        list_cluster.append(int(tokens[4]))
        list_energy.append(float(tokens[3]))
        list_rank.append(int(tokens[0]))
    largest_cluster = max(list_cluster)

    if list_cluster.count(largest_cluster) == 1:
      energy_min = list_energy[list_cluster.index(largest_cluster)]
      rank_of_largest_cluster =  list_rank[list_cluster.index(largest_cluster)]

    else:
      list_min = []
      for j in range(len(list_cluster)):
        if list_cluster[j] == largest_cluster:
          list_min.append(list_energy[j])
      energy_min = min(list_min)
      rank_of_largest_cluster = list_rank[list_cluster.index(largest_cluster)]

    run = 0
    for line in fileinput.input(dlg_file):
      run = run + 1
      if (run >= y+9) and (run < z-1):
        cluster_rank = int(line[0:4])
        binding_energy = float(line[20:32])
        if cluster_rank == rank_of_largest_cluster:
          f.write(list_box[i]+' ')
          f.write("pose_" + str(int (line[15:20])) + ".pdb ")
          f.write(str(binding_energy))
          f.write('\n')

  count = 1
  outfile = ROOT+'/Binding_modes'+'/Rank_'+str(set_x)+'_population_for_'+list_box[i]+"/pose_" + str (count) + ".pdb"

  file = open(outfile, 'w')
  for line in fileinput.input(dlg_file):
    line_str = line
    if ((line_str[0:12] == "DOCKED: ATOM") and (line_str[25:28] == "INH") or (line_str[25:28] == "LIG") or ((line_str[31:34] == "  0"))):
      if (line_str[29:30] == "d"):
        if (line_str[21:22] == "l" or line_str[21:22] == "L") :
          file.write(line_str[8:20] + "Cl" + line_str[22:29] + "    1" + line_str[34:63] + "\n")
        elif (line_str[21:22] == "r" or line_str[21:22] == "R"):
          file.write(line_str[8:20] + "Br" + line_str[22:29] + "    1" + line_str[34:63] + "\n")
        else:
          file.write(line_str[8:29] + "    1" + line_str[34:63] + "\n")
      else:
        if (line_str[21:22] == "l" or line_str[21:22] == "L") :
          file.write(line_str[8:20] + "Cl" +  line_str[22:63] + "\n")
        elif (line_str[21:22] == "r" or line_str[21:22] == "R"):
          file.write(line_str[8:20] + "Br" + line_str[22:29] + "    1" + line_str[34:63] + "\n")
        else:
          file.write(line_str[8:29] + "    1" + line_str[34:63] + "\n")
    if (line_str[0:15] == "DOCKED: TORSDOF"):
      count = count + 1
      file.write("END\n")
      outfile = ROOT+'/Binding_modes'+'/Rank_'+str(set_x)+'_population_for_'+list_box[i]+"/pose_" + str (count) + ".pdb"
      file = open(outfile, 'w')

  os.mkdir('Ranked_poses')
  y = 1
  pose = []
  for line in fileinput.input(path7):
    str_line = str.split(line,'\n')
    str_line = str.split(line,' ')
    str_line = str.split(str_line[1],'.pdb')
    pose.append(str_line[0])

  for j in range(len(pose)):
    os.mkdir('Ranked_poses/Rank_' + pose[j])

    # take file2 as an argument
    path8 = ROOT+'/Binding_modes'+'/Rank_'+str(set_x)+'_population_for_'+list_box[i]+"/Ranked_poses/Rank_" + str (pose[j]) + '/w_fixed_h_'+str(pose[j])+'.pdb' 
    # counter for the ligand limits
    run_c = 1
    run_o = 1
    run_n = 1
    run_h = 1
    run2 = 1

    path9 = ROOT+'/Binding_modes'+'/Rank_'+str(set_x)+'_population_for_'+list_box[i]+"/"+ str (pose[j])+'.pdb'
    file = open(path8, 'w')
    for line in fileinput.input(path9):
      lin_str = line
      if (lin_str[0:6] == "HETATM" or lin_str[0:4] == "ATOM" ):
        if (lin_str[13:14] == "H" or lin_str[14:15] == "H"):
          file.write(lin_str[0:12] + " H" + str(run_h) + ((3 - len (str(run_h))) * " ")  + "UNK" +lin_str[20:54]+'\n')
          run_h = run_h+1
        elif (lin_str[13:14] == "L" or lin_str[13:14] == "l"):
          file.write(lin_str[0:12] + "Cl" + str(run2) + ((3 - len (str(run2))) * " ")  + "UNK" +lin_str[20:54]+'\n')
          run2 = run2+1
        elif (lin_str[13:14] == "C" ):
          file.write(lin_str[0:12] + " C" + str(run_c) + ((3 - len (str(run_c))) * " ")  + "UNK" +lin_str[20:54]+'\n')
          run_c = run_c+1
        elif (lin_str[13:14] == "O" ):
          file.write(lin_str[0:12] + " O" + str(run_o) + ((3 - len (str(run_o))) * " ")  + "UNK" +lin_str[20:54]+'\n')
          run_o = run_o+1
        elif (lin_str[13:14] == "N" ):
          file.write(lin_str[0:12] + " N" + str(run_n) + ((3 - len (str(run_n))) * " ")  + "UNK" +lin_str[20:54]+'\n')
          run_n = run_n+1
        else:
          file.write(lin_str[0:17] + "UNK" + lin_str[20:54]+'\n')

    shutil.move(path9, ROOT+'/Binding_modes'+'/Rank_'+str(set_x)+'_population_for_'+list_box[i]+"/Ranked_poses/Rank_" + str(pose[j]) + '/'+str(pose[j])+'.pdb')
