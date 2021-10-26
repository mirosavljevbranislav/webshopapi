Vagrant.configure("2") do |config|

  # Creating vm for API
  config.vm.define "webshop_api" do |webshop_api|

    #webshop_api.vm.network "public_network", ip: "192.168.0.17"

    webshop_api.vm.box = "hashicorp/bionic64"
    
    webshop_api.vm.network "forwarded_port", guest: 8000, host: 8400

    #webshop_api.vm.synced_folder "/home/bane/test_folder", "/home/vagrant"
    
    webshop_api.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end

    webshop_api.vm.provision "ansible" do |ansible|
      #ansible.host_key_checking = false
      ansible.playbook = "ansible/deploy_api.yml"
    end
    webshop_api.vm.post_up_message = "API deployment successful!"
  end

  # Creating vm for database
  config.vm.define "db" do |db|
    db.vm.box = "hashicorp/bionic64"
    db.vm.network "forwarded_port", guest: 27017, host: 27017

    db.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end

    db.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/deploy_db.yml"
    end

    config.vm.post_up_message = "Database deployment successful!"    
  end



  config.vm.post_up_message = "Deployment successful!"
end
