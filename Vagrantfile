Vagrant.configure("2") do |config|

  # Creating vm for API
  config.vm.define "api" do |api|

    api.vm.box = "hashicorp/bionic64"
    api.vm.network "forwarded_port", guest: 22, host: 8000, protocol: "tcp"

    api.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end

    api.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/deploy_api.yml"
    end
    api.vm.post_up_message = "API deplyoment successfull!"
  end

  # Creating vm for database
  config.vm.define "db" do |db|
    db.vm.box = "hashicorp/bionic64"
    db.vm.network "forwarded_port", guest: 27017, host: 27017

    db.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end

    # Shell scripts for setting up mongodb, docker, python, 
    db.vm.provision "shell", path: "/home/bane/PycharmProjects/webshop_task/shell_scripts/dc_install.sh"
    db.vm.provision "shell", path: "/home/bane/PycharmProjects/webshop_task/shell_scripts/dc_shell.sh" 

    # db.vm.provision "ansible" do |ansible|
    #   ansible.playbook = "ansible/deploy_db.yml"
    # end

    config.vm.post_up_message = "Database deplyoment successfull!"    
  end



  config.vm.post_up_message = "Deplyoment successfull!"
end
