REM force-exclude to make sure it uses the extend-exclude from pyproject.
python -m ruff check ../hhnk_threedi_tools --select I --force-exclude --fix 
python -m ruff format ../python_workflow_demo/**/*.py --force-exclude