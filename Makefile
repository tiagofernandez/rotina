docker_image = rotina/ubuntu

all: run

clean:
	find . -name '*.pyc' -print0 | xargs -0 rm
	rm -rf build/

build: clean
	mkdir -p build/{rotina,requirements}/
	rsync -av rotina/ build/rotina/
	cp requirements/{common,prod}.txt build/requirements
	sed "s/dev/prod/g" manage.py > build/manage.py
	docker build --no-cache --tag="${docker_image}" --rm=true .

shell:
	docker run -t -i rotina/ubuntu /bin/bash

run:
	docker run -e "DB_HOST=${INTERNAL_IP}" -t -i -p 8182:8000 ${docker_image}
