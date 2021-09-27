Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "ansible", playbook: "webshop.yml"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end
  config.vm.provision "docker" do |d|
    d.pull_images "https://github.com/mirosavljevbranislav/webshopapi/blob/9a1304b0b6b48ff31682457ac6e41284f5c8a9e2/.github/workflows/webshop_image.yml"
  end
  # config.vm.provision "shell", path: "/home/bane/PycharmProjects/webshop_task/shell_scripts/dc_install.sh"
  # config.vm.provision "shell", path: "/home/bane/PycharmProjects/webshop_task/shell_scripts/dc_shell.sh"
end
