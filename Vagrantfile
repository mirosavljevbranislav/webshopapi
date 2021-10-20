Vagrant.configure("2") do |config|

  # Creating vm for API
  config.vm.define "api" do |api|

    api.vm.box = "hashicorp/bionic64"
    
    api.vm.network "forwarded_port", guest: 8000, host: 8400, protocol: "tcp"

    api.vm.synced_folder "/home/bane/test_folder", "/home/vagrant"
    
    api.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end

    api.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/deploy_api.yml"
    end
    api.vm.post_up_message = "API deployment successful!"
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
