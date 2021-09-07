#!/bin/bash
echo "DC_INSTALL EXECUTION STARTED"
# Setting up docker, docker-compose, vagrant and python
sudo apt-get update && sudo apt-get -y install docker && sudo apt -y install docker-compose 
curl -O https://releases.hashicorp.com/vagrant/2.2.9/vagrant_2.2.9_x86_64.deb && sudo apt install ./vagrant_2.2.9_x86_64.deb
tar -xvzf Python-3.7.7.tgz && pip install . && python setup.py install

# Docker-compose version fix
compose_version=$(curl https://api.github.com/repos/docker/compose/releases/latest | jq .name -r)
output='/usr/local/bin/docker-compose'
curl -L https://github.com/docker/compose/releases/download/$compose_version/docker-compose-$(uname -s)-$(uname -m) -o $output
chmod +x $output
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
echo "DC_INSTALL EXECUTION FINISHED"