#!/bin/bash
echo "Import MongoDB Public Key - Updated for MongoDB Version 3.6"

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5

echo "Create list file for MongoDB"

echo "deb [ arch=amd64,arm64,ppc64el,s390x ] http://repo.mongodb.com/apt/ubuntu xenial/mongodb-enterprise/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-enterprise.list

sudo apt-get update -y

sudo apt-get install -y mongodb-enterprise

sudo apt-get upgrade -y

echo "Virtual machine provisioned"

