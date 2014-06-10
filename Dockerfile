# References:
# http://docs.docker.io/reference/builder/
# http://docs.docker.io/reference/commandline/cli/

FROM ubuntu:14.04

# Foundation
RUN apt-get update
RUN apt-get install -y software-properties-common python-software-properties python-dev python-setuptools make \
  build-essential libssl-dev libpq-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm git

# Python 3
RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
ENV PATH /.pyenv/bin:$PATH
RUN eval "$(pyenv init -)"
RUN pyenv install 3.4.1
RUN pyenv local 3.4.1

# Virtualenv
RUN easy_install pip
RUN pip install virtualenv
RUN virtualenv -p /.pyenv/versions/3.4.1/bin/python /.virtualenvs/app

# Environment
ADD etc/docker/ /

# Application
EXPOSE 8000
ADD etc/scripts/ scripts/
ADD build/ app/
RUN ./scripts/install.sh
CMD ./scripts/run.sh
