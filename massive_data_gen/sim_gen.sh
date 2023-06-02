#!/bin/bash
# ----------------SLURM Parameters----------------
#SBATCH -J babycal           ## name that will show up in the queue
#SBATCH --mem-per-cpu=8000   # memory per CPU core
#SBATCH -o sbatch_logs/slurm-%j.out  # STDOUT (%j = JobId)
#SBATCH -e sbatch_logs/slurm-%j.err  # STDERR (%j = JobId)

# ----------------Modules-------------------------
source /opt/software/jlab/devel/setup-gcc9.sh

# ----------------Variables------------------------
project=/user/d/dhebel/babycal/bcal/gemc/

# ----------------Comands--------------------------

# Set filename.
nrows="15" # Set by hand based on bcal_geometry!
ncols="15" # Set by hand based on bcal_geometry!

now="$(date +'%Y-%m-%dT%H:%M:%S')"
FNAME="bcal_"$now"_r"$nrows"c"$ncols".txt"

# Access the project directory
cd $project

gemc bcal.gcard -OUTPUT="txt, ../out/$FNAME"

# Loop over the range of simulations
#for ((i=1; i<=10; i++))
#do
#    # Run gemc.
#    gemc bcal.gcard -OUTPUT="txt, ../out/$FNAME"
#    # Wait for 1 second before starting the next simulation
#    sleep 1
#done

# Request a 1000 gemc simulations (sbatch jobs) for the script bcal.gcard in the bcal directory (1 job for every second).
# sbatch --array=1-5000 bcal.gcard -OUTPUT="txt, ../out/$FNAME"

#counter=0
#while [ $counter -lt 10 ]
#do
#    sbatch bcal/run.sh
#    # wait 1 second between jobs
#    sleep 1
#    ((counter++))
#done
