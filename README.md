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

Create the Postgres login role & database:

```
CREATE ROLE rotina LOGIN
  ENCRYPTED PASSWORD 'md54c4d8dbd73e55b4b153395743b3a2339'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;

CREATE DATABASE rotina
  WITH OWNER = rotina
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'C'
       LC_CTYPE = 'C'
       CONNECTION LIMIT = -1;
```

Setup the project:

```
cd rotina
paver setup
```
