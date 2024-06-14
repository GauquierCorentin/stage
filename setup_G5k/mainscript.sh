#!/bin/bash

echo "Mise a jour de la liste des paquets..."
apt update

echo "Installation des dependances necessaires..."
apt install -y build-essential curl

# Installer Rust via rustup
echo "Installation de Rust via rustup..."
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

echo "Ajout de Cargo au PATH..."
source $HOME/.cargo/env

echo "Ajout de Cargo au PATH de maniere persistante..."
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> $HOME/.bashrc

# V  rifier l'installation de Rust et Cargo
echo "Verification de l'installation de Rust et Cargo..."
rustc --version
cargo --version

# Installer rq via Cargo
echo "Installation de rq via Cargo..."
cargo install rsonpath

# V  rifier l'installation de rq
echo "Verification de l'installation de rq..."
rq --version

echo "Installation de rq terminee avec succes."

