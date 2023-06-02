import os
import time

# Run sbatch command (sim_gen.sh) in parallel 3000 times and waiting 1 second between each run
for i in range(5000):
        os.system('bash sim_gen.sh')

# Move all files from /user/d/dhebel/babycal/bcal/out/ to /user/d/dhebel/babycal/src/sims/neutron/
os.system('mv /user/d/dhebel/babycal/bcal/out/* /user/d/dhebel/babycal/src/sims/neutron/')
os.system('echo "Moved all files from /user/d/dhebel/babycal/bcal/out/ to /user/d/dhebel/babycal/src/sims/neutron/"')

# Now for neutron:
for FNAME in os.listdir("/user/d/dhebel/babycal/src/sims/neutron"):
        os.system('bash run.sh /user/d/dhebel/babycal/src/sims/neutron/{} 5 0.3 0.3'.format(FNAME))
        os.system('echo "Gruid translation finished for {}"'.format(FNAME))

# Move all files from /user/d/dhebel/babycal/gruid-translator/out to user/d/dhebel/babycal/src/translations/neutron/
os.system('mv /user/d/dhebel/babycal/gruid-translator/out/* /user/d/dhebel/babycal/src/translations/neutron/')
os.system('echo "Moved all files from /user/d/dhebel/babycal/gruid-translator/out to user/d/dhebel/babycal/src/translations/neutron/"')
