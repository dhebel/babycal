import os

# Access the script's directory (cd /user/d/dhebel/babycal/gruid-translator/)
os.chdir("/user/d/dhebel/babycal/gruid-translator/")

# Iterate over all files in "sims/mu-" and translate them applying the gruid-translator like this $FNAME 5 0.3 0.3
#for FNAME in os.listdir("/user/d/dhebel/babycal/sims/mu-"):
#        os.system('bash run.sh /user/d/dhebel/babycal/sims/mu-/{} 5 0.3 0.3'.format(FNAME))
#        os.system('echo "Gruid translation finished for {}"'.format(FNAME))

# Now for mu+:
#for FNAME in os.listdir("/user/d/dhebel/babycal/sims/mu+"):
#        os.system('bash run.sh /user/d/dhebel/babycal/sims/mu+/{} 5 0.3 0.3'.format(FNAME))
#        os.system('echo "Gruid translation finished for {}"'.format(FNAME))

# Now for neutron:
for FNAME in os.listdir("/user/d/dhebel/babycal/bcal/out/"):
        os.system('bash run.sh /user/d/dhebel/babycal/bcal/out/{} 5 0.3 0.3'.format(FNAME))
        os.system('echo "Gruid translation finished for {}"'.format(FNAME))
