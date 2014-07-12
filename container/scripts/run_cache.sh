#!/bin/bash

echo "Starting cache..."
CMD=${1:-"memcached -u nobody"}
$CMD
