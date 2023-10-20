#!/bin/sh

# Get root privileges
[ "$(whoami)" != "root" ] && exec sudo -- "$0" "$@"

# Get call arguments
CLUSTER_NAME=$1
FOLDER=$2
PORT=$3

sudo -u postgres -- psql -p "$PORT" -d "$CLUSTER_NAME"db -f "$FOLDER"/meteocat_xema.sql
sudo -u postgres -- psql -p "$PORT" -d "$CLUSTER_NAME"db -f "$FOLDER"/meteocat_xdde.sql
