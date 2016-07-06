## Python setup for OSX ##
Install Python 2.7 and Pip somehow.
Install Git.
For example use http://brew.sh/
```bash
sudo -H pip install autoenv
echo 'source /usr/local/opt/autoenv/activate.sh' >> ~/.bash_profile
source ~/.bash_profile

sudo -H pip install virtualenv
sudo -H pip install virtualenvwrapper
echo 'export WORKON_HOME=~/Envs' >> ~/.bash_profile
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bash_profile
source ~/.bash_profile
```
## Python setup for Windows ##
Install Python 2.7 and Pip somehow.
Install Git for Windows (bash).
For example use http://scoop.sh/
```bash
pip install autoenv
echo 'source $(which activate.sh)' >> ~/.bash_profile
source ~/.bash_profile

pip install virtualenv
pip install virtualenvwrapper
echo 'export WORKON_HOME=~/Envs' >> ~/.bash_profile
echo 'source $(dirname $(which virtualenvwrapper_lazy.sh))/virtualenvwrapper.sh' >> ~/.bash_profile
source ~/.bash_profile
```
## Project setup ##
```bash
git clone https://github.com/valentinomiazzo/tilext.git
cd tilext
mkvirtualenv tilext -r requirements.txt
```

## Use ##
```bash
cd tilext
python tilext -i tests/truxton.png -o truxton_test
```

## Test ##
```bash
cd tilext
py.test
```
