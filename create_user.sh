#!/bin/bash


create_user() {
    username=$1
    password=$2

    
    sudo useradd -m -s /bin/bash $username

   
    echo "$username:$password" | sudo chpasswd

   
    echo "User '$username' has been created."
}


read -p "Enter username: " username
read -sp "Enter password: " password
echo


create_user $username $password
