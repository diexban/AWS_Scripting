# AWS_Scripting_App_Project
Showcase Project

## Tools Used
* AWS for Instance Provitioning
* Bash for Scripting
* Python for Scripting
* Markdown for documentation
* PuTTY for testing connectivity from my Windows Computer

## Part 1
Deployed a Amazon Linux EC2 Instance using the AWS Dashboard, making sure that is is associated to the privious key pair created. Connected using the AWS CLI

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

