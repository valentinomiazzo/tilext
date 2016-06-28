## Python setup for OSX ##
```bash
sudo easy_install pip

sudo -H pip install autoenv
echo 'source /usr/local/opt/autoenv/activate.sh' >> ~/.bash_profile
source ~/.bash_profile

sudo -H pip install virtualenv
sudo -H pip install virtualenvwrapper
echo 'export WORKON_HOME=~/Envs' >> ~/.bash_profile
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bash_profile
source ~/.bash_profile
```
## Project setup ##
* Clone this repo in a folder (e.g. project)
```bash
cd tilext
mkvirtualenv tilext -r requirements.txt
```

## Use ##
...

## Test ##
```bash
cd tilext
py.test
```
