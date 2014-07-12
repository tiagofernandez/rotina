FROM ubuntu:14.04

# Foundation
RUN apt-get update
RUN apt-get install -y python3-pip libpq-dev nginx memcached supervisor
RUN apt-get clean

# Application
ADD build /
RUN /scripts/setup.sh
EXPOSE 8080
CMD supervisord
