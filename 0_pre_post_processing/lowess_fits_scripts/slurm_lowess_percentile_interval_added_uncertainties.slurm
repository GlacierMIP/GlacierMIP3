#!/bin/bash
#
#SBATCH --job-name=lowess_fits
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=64
#SBATCH --time=4:00:00
#SBATCH --mail-user=lilian.schuster@student.uibk.ac.at
#SBATCH --mail-type=ALL
#SBATCH --qos=low

# Abort whenever a single step fails. Without this, bash will just continue on errors.
set -e


OGGM_WORKDIR="/work/$SLURM_JOB_USER/$SLURM_JOB_ID/wd"

# Load the required environment modules for OGGM
module load oggm-binary-deps/4 python/3.10 
# Activate our local OGGM virtualenv
#source ~/mambaforge/envs/oggm_gmip3_working/bin/activate
# source ./oggm_venv/bin/activate
# On every node, when slurm starts a job, it will make sure the directory
# /work/username exists and is writable by the jobs user.
# We create a sub-directory there for this job to store its runtime data at.
WORKDIR="/work/$SLURM_JOB_USER/$SLURM_JOB_ID"
mkdir -p "$WORKDIR"

# Export the WORKDIR as environment variable so our script can use it to find its working directory.
export WORKDIR

# Use the local data download cache
export OGGM_DOWNLOAD_CACHE=/home/data/download
export OGGM_DOWNLOAD_CACHE_RO=1
export OGGM_EXTRACT_DIR="/work/$SLURM_JOB_USER/$SLURM_JOB_ID/oggm_tmp"

# Run the actual job. The srun invocation starts it as individual step for slurm.
srun -n 1 -c "${SLURM_JOB_CPUS_PER_NODE}" /home/users/lschuster/images/oggm_20230222.sif bash -s <<EOF
	set -e
    
    python3 -m venv --system-site-packages "$OGGM_WORKDIR/oggm_gmip3_working"
    source "$OGGM_WORKDIR/oggm_gmip3_working/bin/activate"
    pip install moepy
    pip install seaborn
    python3 lowess_percentile_interval_fit_per_region_added_uncertainties.py $1 $2 $3
EOF

#$1 $2
# echo "Start copying..."

# Once a slurm job is done, slurm will clean up the /work directory on that node from any leftovers from that user.
# So copy any result data you need from there back to your home dir!


# Copy any neccesary result data.
# cp -R "${WORKDIR}" "${OUTDIR}/"

# Print a final message so you can actually see it being done in the output log.
echo "SLURM DONE"
