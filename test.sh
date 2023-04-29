#!/bin/bash
# ----------------SLURM Parameters----------------
#SBATCH -p gpuk
#SBATCH -J dnn_02
#SBATCH --mail-user=raquel.pezoa@usm.cl
#SBATCH --mail-type=ALL
#SBATCH -o higgs_output_%j.log
#SBATCH -e higgs_error_%j.log
#SBATCH --gres=gpu:1
#SBATCH --time=7-00:00:00
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
