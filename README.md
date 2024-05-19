# AWS_Scripting_App_Project
Showcase Project

## Tools Used
* AWS for Instance Provitioning
* Bash for Scripting
* Python for Scripting
* Markdown for documentation
* PuTTY for testing connectivity from my Windows Computer
* Git for local and remote repository
* Ansible

## Refereced Documentation
*Github Documentation
*AWS Documentation

## Part 1
Deployed a Amazon Linux EC2 Instance using the AWS Dashboard, making sure that is is associated to the privious key pair created. Connected using the AWS CLI
Created a AWS Billing preference to inform me when my free tier usage is depleted

Proceeded to create a new user called Diego
*sudo adduser Diego*

Loaded up the saved private key on PuTTYgen so I could check the public key
Changed to my newly created user
*sudo su - Diego*

Added Diego to sudo priviledges
*sudo usermod -aG wheel Diego*

Created a new folder in the home directory *mkdir .ssh*

*ls -a* to verify folder creation
*chmod 700 .ssh* 
*touch .ssh/authorized_keys*
*chmod 600 .ssh/authorized_keys*
*vim .ssh/authorized_keys*
*i*
*esc*
*:wq*

*cat authorized_key* To check that the key was inserted correctly

Now I can ssh from PuTTy directly into my created Diego User

Installed Git on the instance
sudo yum install git
checked if it installed git --version
Added create_user to git 
git add create_user.sh
Configured Git with my email and password
git commit -m "Added Script"

Copied this repository as a remote repository
Installed Curl 
sudo yum install curl
Checked Curl version
curl --version
Tried to install the git credential manager via
curl -L https://aka.ms/gcm/linux-install-source.sh | sh
<img width="536" alt="image" src="https://github.com/diexban/AWS_Scripting_App_Project/assets/166546790/cf546bbd-c7d8-4b05-97a9-cbef6b9c310c">

Installed Python
sudo yum install Python

Created a separate Ubuntu Instance to install Ansible





