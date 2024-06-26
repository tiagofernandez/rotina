# Development

Install [Virtualfish](https://github.com/adambrenecki/virtualfish):

    brew update
    brew install fish
    chsh -s /usr/local/bin/fish

Install Python 3 via [Pyenv](https://github.com/yyuu/pyenv):

    brew install pyenv
    pyenv install 3.4.0

Create the virtual environment:

    virtualenv -p ~/.pyenv/versions/3.4.0/bin/python ~/.virtualenvs/rotina
    vf activate rotina

Install the required development tools:

    pip install paver
    npm install -g bower gulp
    brew install memcached

Install [Postgres](http://www.postgresql.org/download/), then create a role and database:

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

Setup the project:

    paver setup

Run the application:

    paver run


## Docker

Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Docker](http://docs.docker.io/installation/mac/), then enable port forwarding:

    VBoxManage modifyvm "boot2docker-vm" --natpf1 "tcp-port8080,tcp,,8080,,8080"
    VBoxManage modifyvm "boot2docker-vm" --natpf1 "udp-port8080,udp,,8080,,8080"

Allow database connections from anywhere:

    sudo sed -i -e "s/^#listen_addresses =.*\$/listen_addresses = '*'/" /Library/PostgreSQL/9.3/data/postgresql.conf
    sudo echo "host    all    all    0.0.0.0/0    md5" >> /Library/PostgreSQL/9.3/data/pg_hba.conf
    sudo su postgres -c "/Library/PostgreSQL/9.3/bin/pg_ctl -m fast -D /Library/PostgreSQL/9.3/data restart"

Build the image:

    make build

Run the container:

    make run

Run the container (detached):

    make run_detached

Run the container (shell):

    make run_shell
