import sys
import glob
import os
import fileinput
import shutil

top_number = int(sys.argv[1])
top_pose = int(sys.argv[2])
path = (sys.argv[3])
receptor_name = (sys.argv[4])
ligand_name = (sys.argv[5])

aux1 = str.split(path,'/summary')
ROOT = aux1[0]

count = 0
box_dock = []
for line in fileinput.input(path):
  if count < top_number:
    line_str = str.split(line,'/')
    folder_index = line_str.index(ligand_name)
    box_dock.append(line_str[folder_index-1])
    count += 1

files = glob.glob(ROOT+'/Binding_modes/Only_the_best_dock/*')
for f in files:
    os.remove(f)

pose = []
box_name = []
binding_energy = []
for i in range(len(box_dock)):
  count = 0
  for line in fileinput.input(ROOT+'/Binding_modes/Rank_1_population_for_'+box_dock[i]+'/pop_list.txt'):
    if count < top_pose:
      line_str = str.split(line,'\n')
      line_str = str.split(line_str[0],' ')
      pose_name = str.split(line_str[1],'.')[0]
      pose.append(pose_name)
      box_name.append(line_str[0])
      binding_energy.append(line_str[2])
      count += 1

path1 = ROOT+'/Binding_modes/Only_the_best_dock/ranking_poses.txt'
with open(path1, 'w') as f:
  for i in range(len(box_dock)):
    f.write(box_name[i]+' '+pose[i]+' '+binding_energy[i])
    f.write('\n')

for i in range(len(box_dock)):
  receptor_path = ROOT+'/Structures/Receptor/'+receptor_name+'.pdb'
  ligand_path = ROOT+'/Structures/Ligand/'+ligand_name+'.pdb'
  w_fixed_h_path = ROOT+'/Binding_modes/Rank_1_population_for_'+box_dock[i]+'/Ranked_poses/Rank_'+pose[i]+'/w_fixed_h_'+pose[i]+'.pdb'
  complex_path = ROOT+'/Binding_modes/Rank_1_population_for_'+box_dock[i]+'/Ranked_poses/Rank_'+pose[i]+'/complex_'+str(i+1)+'.pdb'

  receptor_lines = []
  for line in fileinput.input(receptor_path):
    receptor_lines.append(line)

  w_fixed_lines = []
  for line in fileinput.input(w_fixed_h_path):
    w_fixed_lines.append(line)

  ligand_lines = []
  for line in fileinput.input(ligand_path):
    ligand_lines.append(line)

  with open(complex_path,'w') as f:
    for j in range(len(receptor_lines)):
      if receptor_lines[j][0:4] == "ATOM":
        f.write(receptor_lines[j])
    f.write('TER\n')
    for j in range(len(w_fixed_lines)):
      if w_fixed_lines[j][0:4] == "ATOM":
        f.write(w_fixed_lines[j])
    f.write('TER\n')
    for j in range(len(ligand_lines)):
      if ligand_lines[j][0:4] == "ATOM":
        f.write(ligand_lines[j])
    f.write("END")

  shutil.copy(ROOT+'/dock_here/'+box_dock[i]+'/grid_box.pdb',ROOT+'/Binding_modes/Only_the_best_dock')
  os.rename(ROOT+'/Binding_modes/Only_the_best_dock/grid_box.pdb',ROOT+'/Binding_modes/Only_the_best_dock/grid_box'+str(i+1)+'.pdb')
  shutil.copy(complex_path,ROOT+'/Binding_modes/Only_the_best_dock')
