#!/bin/bash
echo "DC_SHELL EXECUTION STARTED"
mkdir webshop_api
cd webshop_api

git clone https://github.com/mirosavljevbranislav/webshopapi.git && cd WebshopAPi

docker-compose up
echo "DC_SHELL EXECUTION FINISHED"