#!/bin/bash
# ----------------SLURM Parameters----------------
#SBATCH -J babycal    ## name that will show up in the queue
#SBATCH -p batch  ## the partitions to run in (comma seperated)
#SBATCH -n 10  ## number of tasks (analyses) to run
#SBATCH -c 3  ## the number of threads allocated to each task
#SBATCH --mem-per-cpu=8000   # memory per CPU core
#SBATCH --mail-type=ALL   ## email when the job starts, ends, or fails; or you can set this to only fail
#SBATCH --mail-user=daniel.hebel@sansano.usm.cl
#SBATCH -o sbatch_logs/sim_gen_%j.log ## filename of the output; the %j is equal to jobID; default is slurm-[jobID].out
#SBATCH -e sbatch_logs/sim_gen_error_%j.log

# ----------------Modules--------------------------
use anaconda3

# ----------------Variables------------------------
project=/user/d/dhebel/babycal/

# ----------------Comands--------------------------
#Set up environment
conda activate babycal
#Compile GEMC
compile_gemc

#Run GEMC + Gruid
# Execute job steps

srun translated_simulation.sh &
srun translated_simulation.sh &
srun translated_simulation.sh &
srun translated_simulation.sh &
srun translated_simulation.sh &
srun translated_simulation.sh &
srun translated_simulation.sh &
srun translated_simulation.sh &
srun translated_simulation.sh &
srun translated_simulation.sh
wait

#srun bash -c "source translated_simulation.sh" &
#wait
