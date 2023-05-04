#!/bin/bash

#Compile GEMC for every simulation (for now)
compile_gemc

# Set filename.
nrows="7" # Set by hand based on bcal_geometry!
ncols="7" # Set by hand based on bcal_geometry!
#now="$(date +'%Y%m%d%H%M%S')"
now="$(date +'%Y-%m-%dT%H:%M:%S')"
FNAME="bcal_"$now"_r"$nrows"c"$ncols".txt"

# Run gemc.
cd bcal/gemc/
gemc bcal.gcard
cd ../out/
mv "output.txt" $FNAME
echo $FNAME

cd ../../gruid-translator
source run.sh ../bcal/out/$FNAME 30 0.1 0.1
echo "Gruid translation finished for $FNAME"

