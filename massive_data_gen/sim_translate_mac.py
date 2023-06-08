import os

# Access the script's directory (cd /Users/dhebel/babycal/gruid-translator)
os.chdir("/Users/dhebel/babycal/gruid-translator")

# Iterate over all files in "/Users/dhebel/babycal/src/sims/mu-" and translate them applying the gruid-translator like this $FNAME 5 0.3 0.3
for FNAME in os.listdir("/Users/dhebel/babycal/src/sims/mu-"):
        os.system('bash run.sh /Users/dhebel/babycal/src/sims/mu-/{} 5 0.1 0.1'.format(FNAME))
        os.system('echo "Gruid translation finished for {}"'.format(FNAME))

# Move all files from /Users/dhebel/babycal/gruid-translator/out to /Users/dhebel/babycal/src/translations/0.1/mu-/
os.system('mv /Users/dhebel/babycal/gruid-translator/out/* /Users/dhebel/babycal/src/translations/0.1/mu-/')
os.system('echo "Moved all files from /Users/dhebel/babycal/gruid-translator/out to /Users/dhebel/babycal/src/translations/0.1/mu-/"')

# Now for mu+:
for FNAME in os.listdir("/Users/dhebel/babycal/src/sims/mu+"):
        os.system('bash run.sh /Users/dhebel/babycal/src/sims/mu+/{} 5 0.1 0.1'.format(FNAME))
        os.system('echo "Gruid translation finished for {}"'.format(FNAME))
        
# Move all files from /Users/dhebel/babycal/gruid-translator/out to /Users/dhebel/babycal/src/translations/0.1/mu+/
os.system('mv /Users/dhebel/babycal/gruid-translator/out/* /Users/dhebel/babycal/src/translations/0.1/mu+/')
os.system('echo "Moved all files from /Users/dhebel/babycal/gruid-translator/out to /Users/dhebel/babycal/src/translations/0.1/mu+/"')
