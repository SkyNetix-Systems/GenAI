Write-Host "==============================================="
Write-Host " Creating GLOBAL Conda Environment (Python 3.12)"
Write-Host "==============================================="

conda create -n global python=3.12 -y

Write-Host "`nActivating global environment..."
conda activate global

Write-Host "`nInstalling pip-only packages..."
pip install xgboost lightgbm

Write-Host "`nInstalling Conda DS packages..."
conda install -n global -y numpy pandas scipy scikit-learn matplotlib seaborn statsmodels jupyterlab notebook ipykernel

Write-Host "`nInstalling plotly + xgboost + lightgbm (conda-forge)..."
conda install -n global -y -c conda-forge plotly xgboost lightgbm

Write-Host "`nRe-activating environment..."
conda activate global

Write-Host "`nRegistering kernel for Jupyter..."
python -m ipykernel install --user --name global --display-name "Python (global)"

Write-Host "`nVerifying installation..."
python -c "import sys, numpy, pandas, sklearn; print('OK', sys.version, numpy.__version__, pandas.__version__, sklearn.__version__)"

Write-Host "`nListing Jupyter kernels..."
jupyter kernelspec list

Write-Host "`nListing conda environments..."
conda env list

#conda activate global
#jupyter notebook

Write-Host "`nDONE! Your 'global' environment is fully set up. 🔥"
