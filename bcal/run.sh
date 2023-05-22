#!/bin/bash

#Compile GEMC for every simulation (for now)
compile_gemc

# Set filename.
nrows="15" # Set by hand based on bcal_geometry!
ncols="15" # Set by hand based on bcal_geometry!

now="$(date +'%Y-%m-%dT%H:%M:%S')"
FNAME="bcal_"$now"_r"$nrows"c"$ncols".txt"

# Run gemc.
cd bcal/gemc/
gemc bcal.gcard
cd ../out/
mv "output.txt" $FNAME
