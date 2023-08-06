#!/bin/bash

sudo apt update && sudo apt upgrade -y

sudo apt install -y vsftpd
sudo apt install -y python3

sudo ufw allow 20/tcp
sudo ufw allow 21/tcp
sudo ufw allow 22/tcp
sudo ufw allow 4444/tcp

sudo cp our_vsftpd.conf /etc/vsftpd.conf
sudo systemctl restart vsftpd

sudo mkdir -p /var/ftp/pub
sudo chown nobody:nogroup /var/ftp/pub
echo "vsftpd test file" | sudo tee /var/ftp/pub/test.txt

sudo cp new_user.txt /var/ftp/pub/.new_user.txt

sudo useradd garrett
sudo mkdir -p /home/garrett
sudo chown garrett:garrett /home/garrett
sudo usermod -s /bin/bash garrett
sudo echo 'garrett:changeme' | sudo chpasswd

sudo useradd squadcon_svc
sudo mkdir -p /home/squadcon_svc
sudo chown squadcon_svc:squadcon_svc /home/squadcon_svc
sudo usermod -s /bin/bash squadcon_svc
sudo echo 'squadcon_srv:$qu4dC()nP4$$' | sudo chpasswd

sudo useradd squadcon_admin
sudo mkdir -p /home/squadcon_admin
sudo chown squadcon_admin:squadcon_admin /home/squadcon_admin
sudo usermod -s /bin/bash squadcon_admin
sudo echo 'squadcon_admin:SC!pi_ctf' | sudo chpasswd

sudo useradd pi_svc
sudo mkdir -p /home/pi_svc
sudo chown pi_svc:pi_svc /home/pi_svc
sudo usermod -s /bin/bash pi_svc
sudo echo 'pi_svc:Itis$ecure' | sudo chpasswd

sudo cp our_sudoers /etc/sudoers

sudo useradd ghv_admin
sudo mkdir -p /home/ghv_admin
sudo chown ghv_admin:ghv_admin /home/ghv_admin
sudo usermod -s /bin/bash ghv_admin
sudo echo 'ghv_admin:P@$$w0rd' | sudo chpasswd

sudo apt install -y python3-pip
sudo pip3 install pycrypto

sudo mkdir -p /var/cmd
sudo cp cmd_service.py /var/cmd/.cmd_service.py
sudo chmod +x /var/cmd/.cmd_service.py

sudo cp cmd.service /etc/systemd/system/cmd.service

sudo systemctl daemon-reload
sudo systemctl enable cmd.service
sudo systemctl restart cmd.service

echo 'pi{56ca65bbb1b3b1cdad67aa324a1626d6}' | sudo tee /home/garrett/user.txt
sudo chown garrett:garrett /home/garrett/user.txt

echo 'pi{cfbbd2d6ba6d92ab5b8fe94fa3bbbce7}' | sudo tee /home/ghv_admin/.admin_flag.txt
sudo chown ghv_admin:ghv_admin /home/ghv_admin/.admin_flag.txt

sudo ufw enable

sudo echo 'ubuntu:P@$$w0rd_ubuntu' | sudo chpasswd
sudo echo 'ghv:P@$$w0rd_ghv' | sudo chpasswd

unset HISTFILE
