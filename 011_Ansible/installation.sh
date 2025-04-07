#!/bin/bash

echo "📦 Updating package list..."
sudo apt update

echo "⬆️ Upgrading packages..."
sudo apt upgrade -y

echo "📋 Checking OS version..."
lsb_release -a

echo "➕ Adding Ansible PPA..."
sudo add-apt-repository --yes --update ppa:ansible/ansible

echo "🔄 Updating package list again..."
sudo apt update

echo "🚀 Installing Ansible..."
sudo apt install -y ansible

echo "✅ Verifying Ansible version..."
ansible --version

echo "🎉 Ansible installation completed successfully!"
