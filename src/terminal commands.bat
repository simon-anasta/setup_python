:: terminal commands for Python projects

:: --------------------------------------------------------
:: uv setup

:: create a new project
uv init projectname

:: install the latest versoin of python
uv python install

:: check version of uv
uv version

:: craete a virtual environment
uv venv

:: --------------------------------------------------------
:: uv package management

:: install a package
uv pip install packagename
:: install a package with options
uv pip install 'polars[pandas, numpy]'

:: add a package as a dependency, installing if necessary
uv add packagename

:: check installed pacakges
uv pip list

:: remove packages
uv remove packagename

:: update projects lockfile
uv lock

:: install all dependencies for a previous project
uv sync

:: --------------------------------------------------------
:: running code

:: run specific file
uv run filename.py

:: run python at the terminal
uv run python
:: use `exit()` to close

:: --------------------------------------------------------
:: Jupyter

:: launch Jupyter Lab
uv run jupyter lab
:: then run URL in browser

:: activate a virtual environment
.venv\Scripts\activate

:: --------------------------------------------------------
:: git

:: create a git repository in the current file
git init

:: all your familiar commands work here
git add ./filename
git commit -m "message"
git status
:: etc

:: --------------------------------------------------------
:: other

:: locate the python executable
Get-Command python
