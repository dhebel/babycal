#!/bin/bash

# Compile gemc.
compile_gemc

# Set filename.
nrows="21" # Set by hand based on bcal_geometry!
ncols="21" # Set by hand based on bcal_geometry!

now="$(date +'%Y-%m-%dT%H:%M:%S')"
FNAME="bcal_"$now"_r"$nrows"c"$ncols".txt"

# Run gemc.
cd /user/d/dhebel/babycal/bcal/gemc/
gemc bcal.gcard
cd /user/d/dhebel/babycal/bcal/out/
mv "output.txt" $FNAME
echo $FNAME

cd /user/d/dhebel/babycal/gruid-translator/
source run.sh /user/d/dhebel/babycal/bcal/out/$FNAME 0.1 0.1 0.1
echo "Gruid translation finished for $FNAME"

#cp out/"'out_'$FNAME" ../sims/mu+/
#echo "Copied $FNAME to sims/mu+/"

#cd ..
#echo "Done."
