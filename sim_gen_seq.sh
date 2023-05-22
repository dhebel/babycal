#!/bin/bash
# ----------------SLURM Parameters----------------
#SBATCH -J babycal           ## name that will show up in the queue
#SBATCH --mail-type=ALL      ## email when the job starts, ends, or fails; or you can set this to only fail
#SBATCH --mail-user=daniel.hebel@sansano.usm.cl
#SBATCH -o sbatch_logs/sim_gen_seq_%j.log ## filename of the output; the %j is equal to jobID; default is slurm-[jobID].out
#SBATCH -e sbatch_logs/sim_gen_seq_%j.err ## filename of the error log; default is slurm-[jobID].err

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

# Loop over the range of simulations
for ((i=1; i<=10; i++))
do
    # Run gemc.
    gemc bcal.gcard -OUTPUT="txt, ../out/$FNAME"
    # Wait for 1 second before starting the next simulation
    sleep 1
done

# Request a 1000 gemc simulations (sbatch jobs) for the script bcal.gcard in the bcal directory (1 job for every second).
# sbatch --array=1-1000 bcal.gcard -OUTPUT="txt, ../out/$FNAME"

#counter=0
#while [ $counter -lt 10 ]
#do
#    sbatch bcal/run.sh
#    # wait 1 second between jobs
#    sleep 1
#    ((counter++))
#done
