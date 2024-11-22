for run
```
python -m venv env

# activate env for Windows
env/script/Activate.ps1
# activate env for linux
source env/bin/activate

pip install -r requirements.txt
# all file and text
py.test

# all file and text
py.test -s

# only file
py.test -s -v test_api.py
```