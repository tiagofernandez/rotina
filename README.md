# Development

## Project setup

Install [Virtualfish](https://github.com/adambrenecki/virtualfish):

```
brew update
brew install fish
chsh -s /usr/local/bin/fish
```

Install Python 3.4.0 via [Pyenv](https://github.com/yyuu/pyenv):

```
brew install pyenv
pyenv install 3.4.0
```

Create the virtual environment:

```
virtualenv -p ~/.pyenv/versions/3.4.0/bin/python ~/.virtualenvs/rotina
vf activate rotina
```

Install the required development tools:

```
pip install paver
gem install sass
npm install -g bower gulp
```

Create the Postgres database:
* database name: `rotina`
* login role: `rotina`

Setup the project:

```
cd rotina
paver setup
```
