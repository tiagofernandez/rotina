# Example:
# https://index.docker.io/u/preznik/django-helloworld/

# DOCKER-VERSION 0.9.1
FROM ubuntu:14.04

# Foundation
RUN apt-get install -y software-properties-common python-software-properties python-dev python-setuptools
RUN apt-get install -y make build-essential libssl-dev libpq-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm git

# Repositories
RUN add-apt-repository -y ppa:fkrull/deadsnakes
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get update

# Pyenv
RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
ENV PATH $HOME/.pyenv/bin:$PATH
RUN eval "$(pyenv init -)"
RUN pyenv install 3.4.1
RUN pyenv local 3.4.1

# Virtualenv
RUN easy_install pip
RUN pip install virtualenv
RUN pip install virtualenvwrapper
RUN virtualenv -p $HOME/.pyenv/versions/3.4.1/bin/python $HOME/.virtualenvs/rotina

# Application
ADD scripts/ $HOME/
ADD build/ $HOME/rotina/
RUN ./$HOME/setup.sh
EXPOSE 8000

CMD ./$HOME/run.sh
