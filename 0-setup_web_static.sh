#!/usr/bin/env bash
# Setup webserver to deploy AirBnB-Web static

sudo apt-get update -qq
sudo apt install nginx -y -qq
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/releases/test
sudo chown -R ubuntu:ubuntu /data/

sudo rm -f /data/web_static/releases/test/index.html
sudo touch /data/web_static/releases/test/index.html

printf "<HTML>\n
	 <head>\n
	  <title>HbnB Test Page</title>\n
	 </head>\n
	 <body>\n
	   <h1>Hello HBnB</h1>\n
	 </body>\n
	</html>" | sudo tee -a /data/web_static/releases/test/index.html > /dev/null

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo nginx -s reload
