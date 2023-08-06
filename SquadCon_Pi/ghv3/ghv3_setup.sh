#!/bin/bash

sudo apt-get update
sudo apt-get upgrade -y

# Install vsftpd, python, python3 and python3-pip
sudo apt-get install -y vsftpd
sudo apt-get install -y python
sudo apt-get install -y python3
sudo apt-get install -y apache2
sudo apt-get install -y php


# Change SSH config
sudo cp our_sshd_config /etc/ssh/sshd_config
sudo systemctl restart sshd

# Change config to allow anonymous access
sudo cp vsftpd.conf /etc/vsftpd.conf
sudo mkdir /var/www/html/secret/
sudo chown ftp:ftp /var/www/html/secret/
sudo chmod -R 775 /var/www/html/secret/

sudo systemctl restart vsftpd

# Install python3 pip in order to install pycrypto
sudo apt-get install -y python3-pip
sudo pip3 install pycrypto

# Move cmd_service to directory
sudo mkdir -p /var/cmd/
sudo cp door_key.py /var/cmd/.cmd_service.py
sudo chmod +x /var/cmd/.cmd_service.py
sudo cp cmd.service /etc/systemd/system/cmd.service

# Give www-data sudo access
echo "www-data  ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/www-data

# Plant root flag
sudo echo "pi{sh3s3llsw3bsh3lls}" > /root/.flag.txt

sudo useradd squadcon_srv
sudo mkdir -p /home/squadcon_svc
sudo chown squadcon_svc:squadcon_svc /home/squadcon_svc
sudo usermod -s /bin/bash squadcon_svc
sudo echo 'squadcon_svc:$qu4dC()nP4$$' | sudo chpasswd

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

# Delete command history
history -c
