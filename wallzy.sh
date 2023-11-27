#!/bin/bash

# Base URL
base_url="https://wallzy.onrender.com/"

# Allowed options
allowed_options=("nature" "ghibli" "city" "abstract" "painting" "digital_art" "comfy" "best")

# Check if an argument is provided and if it's one of the allowed options
if [ -z "$1" ]; then
    image_url="${base_url}random"
elif [[ " ${allowed_options[*]} " == *" $1 "* ]]; then
    image_url="${base_url}$1"
else
    echo "Usage: $0 [nature | ghibli | city | abstract | painting | digital_art | comfy | best | abstract]"
    exit 1
fi

# Directory to save the image
wallpaper_dir="$HOME/Pictures/Wallzy-Walls"
mkdir -p "$wallpaper_dir" # Create the directory if it doesn't exist

# File to save the image
image_file="$wallpaper_dir/background.jpg"

# Download the image
curl -L -o "$image_file" "$image_url"

# Set the image as the desktop background (Modern GNOME-based systems only)
if [[ `gsettings get org.gnome.desktop.interface color-scheme` =~ 'dark' ]]; then
	gsettings set org.gnome.desktop.background picture-uri-dark "file://$image_file"
else
	gsettings set org.gnome.desktop.background picture-uri "file://$image_file"
fi
