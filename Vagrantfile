Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end
  config.vm.provision "shell", path: "/home/bane/PycharmProjects/webshop_task/dc_install.sh"
  config.vm.provision "shell", path: "/home/bane/PycharmProjects/webshop_task/dc_shell.sh"
end
