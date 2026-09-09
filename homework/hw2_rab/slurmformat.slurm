#!/bin/bash
#SBATCH --job-name=ast4762
#SBATCH --output=slurm-%j.out
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=4G

# edit this line with your username and python script
/home/ro235529/.conda/envs/ast4762/bin/python3 hw2_rab.py
