#!/usr/bin/env bash
# set up webstatic

server="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
file="/etc/nginx/sites-available/default"
# update apt repos
sudo apt-get update -y
# isntall nginx
sudo apt-get install nginx -y
# recursively create directories
sudo mkdir -p "/data/web_static/releases/test/"
# recursively create directories
sudo mkdir "/data/web_static/shared/"
# Create dummy index.html file
echo "Holberton" >"/data/web_static/releases/test/index.html"
# remove symbolic links
rm -f "/data/web_static/current"
# create symbolic links
ln -s "/data/web_static/releases/test/" "/data/web_static/current"
# change ownership of dir and files, including sym links
sudo chown -hR ubuntu:ubuntu "/data/"
#
sudo sed -i "29i\ $server" "$file"

sudo service nginx restart
