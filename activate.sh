#!/usr/bin/env bash

# Activate the conda environment for assignment 2

ENV_NAME="assignment2"

echo "Activating $ENV_NAME environment..."

# Source conda (adjust if installation path differs)
if [ -f "$HOME/miniconda3/etc/profile.d/conda.sh" ]; then
  . "$HOME/miniconda3/etc/profile.d/conda.sh"
elif [ -f "$HOME/anaconda3/etc/profile.d/conda.sh" ]; then
  . "$HOME/anaconda3/etc/profile.d/conda.sh"
else
  export PATH="$HOME/miniconda3/bin:$PATH"
fi

if ! command -v conda >/dev/null 2>&1; then
  echo "Error: conda not available on PATH. Install or fix your conda setup."
  return 1 2>/dev/null || exit 1
fi

# Create env if missing
if ! conda env list | awk '{print $1}' | grep -qx "$ENV_NAME"; then
  echo "Conda env '$ENV_NAME' not found. Creating from environment.yml..."
  conda env create -f environment.yml || { echo "Env creation failed"; return 1 2>/dev/null || exit 1; }
fi

conda activate "$ENV_NAME" || { echo "Failed to activate $ENV_NAME"; return 1 2>/dev/null || exit 1; }

python -c "import sys; print('Python', sys.version)"
which python

echo
echo "Tip: 'source activate.sh' to keep this shell in the env."
