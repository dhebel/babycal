#!/bin/bash

# Compile gemc.
compile_gemc

# Set filename.
nrows="15" # Set by hand based on bcal_geometry!
ncols="15" # Set by hand based on bcal_geometry!

now="$(date +'%Y-%m-%dT%H:%M:%S')"
FNAME="bcal_"$now"_r"$nrows"c"$ncols".txt"

# Run gemc.
cd /user/d/dhebel/babycal/bcal/gemc/
gemc bcal.gcard -OUTPUT="txt, ../out/$FNAME"
echo $FNAME

cd /user/d/dhebel/babycal/gruid-translator/
source run.sh /user/d/dhebel/babycal/bcal/out/$FNAME 5 0.3 0.3
echo "Gruid translation finished for $FNAME"
