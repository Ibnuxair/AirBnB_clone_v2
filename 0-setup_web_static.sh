#!/usr/bin/env bash
# Install Nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directory structure
if [ ! -d "/data/" ]; then
    sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
fi

# Remove existing symbolic link if it exists
if [ -L "/data/web_static/current" ]; then
    sudo rm -f /data/web_static/current
fi

# Create symbolic link
sudo ln -snf /data/web_static/releases/test /data/web_static/current

# Create or update HTML content
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Set ownership to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i 's|^.*server_name.*$|&\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n|' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
