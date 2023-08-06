#!/bin/bash

sudo apt install -y vsftpd
sudo apt install -y python3
sudo apt install -y python3-pip
sudo pip install flask pyinstaller apscheduler
sudo pip3 install pycrypto
sudo ufw disable

sudo cp our_vsftpd.conf /etc/vsftpd.conf
sudo systemctl restart vsftpd

sudo mkdir -p /var/ftp/pub
sudo chown nobody:nogroup /var/ftp/pub
echo "vsftpd test file" | sudo tee /var/ftp/pub/test.txt

sudo cp new_user.txt /var/ftp/pub/.new_user.txt

sudo cp our_sudoers /etc/sudoers

sudo mkdir /root/dist
sudo cp web_server /root/dist/web_server
sudo chmod +x /root/dist/web_server
sudo cp webflag.service /etc/systemd/system/webflag.service

sudo systemctl daemon-reload
sudo systemctl enable webflag.service
sudo systemctl restart webflag.service

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