#!/bin/bash

# Function to create a new user
create_user() {
    username=$1
    password=$2

    # Create the user with the specified username
    sudo useradd -m -s /bin/bash $username

    # Set the user's password
    echo "$username:$password" | sudo chpasswd

    # Confirm user creation
    echo "User '$username' has been created."
}

# Ask for the user's details
read -p "Enter username: " username
read -sp "Enter password: " password
echo

# Create the user
create_user $username $password
