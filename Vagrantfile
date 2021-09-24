Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "ansible", playbook: "webshop.yml"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end
  config.vm.provision "docker" do |d|
    d.pull_images "https://github.com/mirosavljevbranislav/webshopapi/blob/9add25b82f8b6df52709bac597916e30e2915090/.github/workflows/**"
  end
  # config.vm.provision "shell", path: "/home/bane/PycharmProjects/webshop_task/shell_scripts/dc_install.sh"
  # config.vm.provision "shell", path: "/home/bane/PycharmProjects/webshop_task/shell_scripts/dc_shell.sh"
end
