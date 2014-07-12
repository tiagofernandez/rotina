#!/bin/bash

echo "Starting reverse proxy..."
CMD=${1:-"nginx -c /etc/nginx/nginx.conf"}
$CMD
