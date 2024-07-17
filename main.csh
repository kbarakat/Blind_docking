#!/bin/csh

set ROOT = `pwd`

echo "************* Step 1: Create Dynamic Centers *************"

echo "Please enter the name (or number) of your folder . . ."
set folder_name = $<

set ligand_name = 1T64_KEY
set receptor_name = 1T64_LOCK

set n_atom = 20

set nx = 50
set ny = 50
set nz = 50

set space = 0.75

mkdir $folder_name
mkdir $folder_name/MSMS_files
mkdir $folder_name/Exposed_atoms_and_centers
cp -r $ROOT/Structures $ROOT/$folder_name

cd $ROOT/MSMS

$ROOT/MSMS/pdb_to_xyzrn $ROOT/$folder_name/Structures/Receptor/$receptor_name.pdb > $ROOT/$folder_name/MSMS_files/$receptor_name.xyzr

$ROOT/MSMS/msms.x86_64Linux2.2.6.1 -if $ROOT/$folder_name/MSMS_files/$receptor_name.xyzr -af $ROOT/$folder_name/MSMS_files/$receptor_name > $ROOT/$folder_name/MSMS_files/msms_output.tmp

if (-z $ROOT/$folder_name/msms_output.tmp) then
        echo "Files creation failed!"
else
        echo "Files created successfully!"
endif

rm $ROOT/$folder_name/MSMS_files/msms_output.tmp

cd $ROOT/$folder_name/Exposed_atoms_and_centers

python $ROOT/Python_files/get_surface_exposed_atoms_list.py $ROOT/$folder_name/MSMS_files/$receptor_name.area > surface_exposed_atoms_list.txt
python $ROOT/Python_files/write_information_about_centers.py $ROOT/$folder_name/MSMS_files/$receptor_name.area $ROOT/$folder_name/Structures/Receptor/$receptor_name.pdb $n_atom > centers_info.txt
python $ROOT/Python_files/write_centers.py $ROOT/$folder_name/MSMS_files/$receptor_name.area $ROOT/$folder_name/Structures/Receptor/$receptor_name.pdb $n_atom > centers
python $ROOT/Python_files/exposed_atoms_pdb.py $ROOT/$folder_name/MSMS_files/$receptor_name.area $ROOT/$folder_name/Structures/Receptor/$receptor_name.pdb $ROOT/$folder_name/Exposed_atoms_and_centers/surface_exposed_atoms.pdb

echo "************* Step 2: Ligand and Receptor Preparation *************"

cd $ROOT/$folder_name/Structures/Receptor

set prepare_receptor4 = `which prepare_receptor4.py`
python2 $prepare_receptor4 -r $receptor_name.pdb > receptor_prepare.tmp

python $ROOT/Python_files/Gasteiger_ZN.py $ROOT/$folder_name/Structures/Receptor/receptor_prepare.tmp $ROOT/$folder_name/Structures/Receptor/$receptor_name.pdbqt

echo "Receptor and ligand have been prepared!"
echo "Presiona enter para continuar..."
set continuar = $<

cd $ROOT/$folder_name/Structures/Ligand

set prepare_ligand4 = `which prepare_ligand4.py`
python2 $prepare_ligand4 -l $ligand_name.pdb -U ' '

# path for /MGLToolsPckgs

set aux1 = $prepare_receptor4:h:h
set aux1 = $aux1"/MGLToolsPckgs/AutoDockTools/Utilities24"
set prepare_dpf4 = $aux1"/prepare_dpf4.py"
set prepare_gpf4 = $aux1"/prepare_gpf4.py"
set summarize_results4 = $aux1"/summarize_results4.py"

echo "************* Step 3: Create Docking Folders *************"

mkdir $ROOT/$folder_name/Dock_here
mkdir $ROOT/$folder_name/Summary

cd $ROOT/$folder_name/Dock_here

set count = 0
foreach center (`cat $ROOT/$folder_name/Exposed_atoms_and_centers/centers`)
        mkdir Dock_$count
        cp $ROOT/$folder_name/Structures/Receptor/$receptor_name.pdbqt Dock_$count
        cp $ROOT/$folder_name/Structures/Ligand/$ligand_name.pdbqt Dock_$count
        cd Dock_$count
        python2 $prepare_dpf4 -l $ligand_name.pdbqt -r $receptor_name.pdbqt -p ga_num_evals=5000000 -p ga_pop_size=300 -p ga_run=50 -p rmstol=2.0 -p tstep=1.0 -p qstep=25.0 -p dstep=25.0 -p ga_num_generations=30000
        python2 $prepare_gpf4 -l $ligand_name.pdbqt -r $receptor_name.pdbqt
        set aux2 = `pwd`
        python $ROOT/Python_files/prepare_gpf4_modified.py $aux2/$receptor_name.gpf $nx $ny $nz $space $center
        python $ROOT/Python_files/grid_box.py $aux2/$receptor_name.gpf $aux2"/grid_box.pdb"
        set aux3 = $aux2:h:h
        python $ROOT/Python_files/all_grid_box.py $aux2/$receptor_name.gpf $aux3"/grid_box.pdb"
        set aux4 = `which autogrid4`
        $aux4 -p $aux2/$receptor_name.gpf -l $aux2/$receptor_name.glg
        adgpu_cuda --ffile $aux2/$receptor_name.maps.fld --lfile $aux2/$ligand_name.pdbqt --nrun 100 --rmstol 2 --clustering 1 --psize 250 --nev 10000000
        python2 $summarize_results4 -d $aux2 -t 2.0 -L -a -o $ROOT/$folder_name/Dock_here/Dock_$count"/summary_2.0.txt"
        python2 $summarize_results4 -d $ROOT/$folder_name/Dock_here/Dock_$count -t 2.0 -L -a -o $ROOT/$folder_name/Summary/summary_2.0.txt
        cd ..
        @ count = $count + 1
        end

sort -k5n -t , $ROOT/$folder_name/Summary/summary_2.0.txt > $ROOT/$folder_name/Summary/summary_2.sort

echo "************* Step 4: Analysis *************"

set pop_limit = 3

python $ROOT/Python_files/modify_summary_file.py $ROOT/$folder_name/Summary/summary_2.sort $pop_limit > $ROOT/$folder_name/Summary/modified_summary.sort
python $ROOT/Python_files/get_poses.py $ROOT/$folder_name/Dock_here $ligand_name

set top_number = 10
set top_pose = 1
set summary_path = $ROOT/$folder_name/Summary/modified_summary.sort

python $ROOT/Python_files/get_complex.py $top_number $top_pose $summary_path $receptor_name $ligand_name














