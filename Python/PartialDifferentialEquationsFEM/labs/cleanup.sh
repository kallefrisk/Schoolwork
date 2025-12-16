#!/bin/bash
# =====================================================
# Ubuntu Cleanup Script: Wipes all users and non-essential files
# while keeping the OS intact.
# =====================================================

set -euo pipefail

# --- Step 0: Safety check ---
CURRENT_USER=$(whoami)
echo "Running as: $CURRENT_USER"
read -p "This will delete all users except system accounts. Continue? [y/N]: " confirm
if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo "Aborted."
    exit 1
fi

# --- Step 1: Remove all non-system users (UID >= 1000) ---
echo "Removing non-system users..."
awk -F: '($3>=1000){print $1}' /etc/passwd | grep -v "$CURRENT_USER" | while read user; do
    echo "Deleting user: $user"
    sudo deluser --remove-home "$user"
done

# --- Step 2: Remove user files outside home directories ---
echo "Removing user files in /opt, /usr/local, /srv, /var/www..."
for dir in /opt /usr/local /srv /var/www; do
    if [ -d "$dir" ]; then
        echo "Cleaning $dir..."
        sudo rm -rf "$dir"/*
    fi
done

# --- Step 3: Clean package cache and remove unnecessary packages ---
echo "Cleaning up packages..."
sudo apt-get autoremove --purge -y
sudo apt-get clean

# --- Step 4: Optional: reset default skeleton configs ---
echo "Resetting skeleton configs..."
sudo cp -rn /etc/skel/. /etc/ || true

# --- Finished ---
echo "Cleanup complete. System should remain bootable."
