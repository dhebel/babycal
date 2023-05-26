import os
import time

# Run sbatch command (sim_gen.sh) in parallel 3000 times and waiting 1 second between each run
for i in range(500):
        os.system('sbatch sim_gen.sh')
        time.sleep(2)
