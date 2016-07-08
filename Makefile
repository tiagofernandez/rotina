DOCKER_CONTAINER = rotina
DOCKER_IMAGE = ${DOCKER_CONTAINER}/application

LOCAL_IP = ${shell ifconfig en1 | sed -En 's/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p'}

LOGS_PATH = ${shell pwd}/logs

clean:
	find . -name '*.pyc' -print0 | xargs -0 rm
	rm -rf build

build: clean
	cp -r container build
	rsync -av {rotina,requirements} build/app
	sed "s/dev/prod/g" manage.py > build/app/manage.py
	./manage.py collectstatic --noinput
	cp -r static build/app/static
	docker build --no-cache --tag="${DOCKER_IMAGE}" --rm=true .

run:
	docker run -e "DB_HOST=${LOCAL_IP}" -p 8080:8080 --name ${DOCKER_CONTAINER} -v ${LOGS_PATH}:/logs -t -i ${DOCKER_IMAGE}

run_detached:
	docker run -e "DB_HOST=${LOCAL_IP}" -p 8080:8080 --name ${DOCKER_CONTAINER} -v ${LOGS_PATH}:/logs -d ${DOCKER_IMAGE}

run_shell:
	docker run -e "DB_HOST=${LOCAL_IP}" -p 8080:8080 --name ${DOCKER_CONTAINER} -v ${LOGS_PATH}:/logs -t -i ${DOCKER_IMAGE} /bin/bash
