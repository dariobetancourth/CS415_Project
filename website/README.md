# cs415_website Install Notes

## EC2 Install Commands
## Ubuntu
- Allow Inbound Rules
  - SSH
  - HTTP
  - HTTPS
- Attach IAM Role to Instance
- User Data
    ```
    #!/bin/bash
    sudo apt update -y
    sudo apt install ruby wget -y
    cd /home/ubuntu
    sudo wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install
    sudo chmod +x ./install
    sudo ./install auto
    sudo apt install -y apache2
    sudo systemctl start apache2
    sudo systemctl enable apache2
    ```
## SSH into the Instance
- Validate CodeDeploy Agent is installed and running:
  `sudo service codedeploy-agent status`
- Validate Apache is installed and running:
  `sudo systemctl status apache2`

## Deploy Notes
- Deploy build files into:
  `/var/www/html/`
