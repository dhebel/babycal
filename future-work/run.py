import os, time
import subprocess

# --------- Data generation Phase ---------
# Set number of rows and columns for the BCAL GEMC Architecture.
nrows = "7" # Set by hand based on bcal_geometry!
ncols = "7" # Set by hand based on bcal_geometry!

# Set output file name.
filename = "bcal_" + time.strftime("%Y-%m-%dT%H:%M:%S") + "_r" + nrows + "c" + ncols + ".txt"

# IDEAS:
# READ PARTICLE TYPE FROM GEMC CARD AND ADD IT TO THE FILENAME
# READ ENERGY FROM GEMC CARD AND ADD IT TO THE FILENAME
# READ NUMBER OF EVENTS FROM GEMC CARD AND ADD IT TO THE FILENAME
# SI ... AÑADIR LOS TRES
# Current name format: bcal_2023-04-05T08:12:03_r7c7.txt

os.chdir("../bcal/gemc/")
# Run GEMC... Subprocess is necessary to run GEMC in the background inheriting the environment variables. (?)
gemc = subprocess.Popen(["gemc", "bcal.gcard"])
os.waitpid(gemc.pid, 0)

# Rename output file.
os.chdir("../out/")
os.rename("output.txt", filename)

# --------- Data translation Phase ---------
# Pass simulation output to Gruid Translator.
#os.echo("Leaving GEMC to Translate Data...")
os.chdir("../../gruid-translator/src/")
gruid = subprocess.Popen(["python3", "main.py", "../../bcal/out/" + filename, "30", "0.1", "0.1"])
# Gruid Parameters (Chosen by hand):
# 30 is:  dt    length of each time step for the generated time series in ns.
# 0.1 is: dx    length of each row for each of the time series' matrices in cm.
# 0.1 is: dy    length of each column for each of the time series' matrices in cm.
os.waitpid(gruid.pid, 0)

# --------- Data analysis Phase ---------
# Pass gruid output to Gruid Analyzer.
