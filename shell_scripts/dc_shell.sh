#!/bin/bash
echo "DC_SHELL EXECUTION STARTED"
mkdir webshop_api
cd webshop_api

git clone https://Bangie01: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@github.com/Bangie01/WebshopAPi.git && cd WebshopAPi

docker-compose up
echo "DC_SHELL EXECUTION FINISHED"