#!/bin/bash
# ----------------SLURM Parameters----------------
#SBATCH -J babycal
#SBATCH -p gpuk
#SBATCH -n 1
#SBATCH --gres=gpu:1
#SBATCH -c 2
#SBATCH --mail-user=daniel.hebel@sansano.usm.cl
#SBATCH --mail-type=ALL
#SBATCH --array=1-3%3
#SBATCH -o higgs_output_%j.log
#SBATCH -e higgs_error_%j.log

# ----------------Modules-----------------------------
use anaconda3

# ----------------Variables--------------------------
project=/user/r/rpezoa/HEP_analysis/ATLASImbalanceLearning/

# ----------------Comands--------------------------
source activate /user/r/rpezoa/.conda/envs/root_py
echo "Running test.sh"
echo ""
conda info

cd "$project/scripts"

python best_xgboost_max_gpu.py binary:logistic auc 2022-06-28-binlog_auc_model_5000
