#!/bin/bash
echo "DC_SHELL EXECUTION STARTED"

git clone https://github.com/mirosavljevbranislav/webshopapi.git && cd webshopapi

docker-compose up
echo "DC_SHELL EXECUTION FINISHED"