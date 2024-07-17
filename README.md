# Blind Docking process

Once you have cloned this folder, follow the next steps to perform Blind Docking process.

```zsh
git clone -q https://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@github.com/Mike97179/Blind_docking.git
```

## MGL Tools installation

To create a new environment:

```zsh
conda create --name env_name
```

Activate the new environment:

```zsh
conda activate env_name
```

Update all the environments:

```zsh
conda update --all
```

Run the following command line:

```zsh
conda install -c conda-forge -c bioconda -c hcc mgltools adfr-suite -y
```

There are some errors that you should repair after executing the above command line, don't forget to change the environment name (`env_name`) and unix_name (`test`):

```zsh
cp /home/test/anaconda3/envs/env_name/MGLToolsPckgs/AutoDockTools/interactiveHistogramGraph.py /home/test/anaconda3/envs/env_name/CCSBpckgs/AutoDockTools
```

```zsh
cp -r /home/test/anaconda3/envs/env_name/MGLToolsPckgs/PyAutoDock /home/test/anaconda3/envs/env_name/CCSBpckgs
```

```zsh
mkdir /home/test/.mgltools/
```

```zsh
cp /home/test/anaconda3/envs/env_name/bin/pythonsh /home/test/.mgltools/
```

## MSMS installation

```zsh
wget https://ccsb.scripps.edu/msms/download/933/msms_i86_64Linux2_2.6.1.tar.gz
```

```zsh
tar zxvf msms_i86_64Linux2_2.6.1.tar.gz
```

## AutoDock GPU installation

```zsh
https://github.com/ccsb-scripps/AutoDock-GPU/wiki/Guideline-for-users
```

