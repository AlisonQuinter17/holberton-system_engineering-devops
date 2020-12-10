#!/usr/bin/env bash
# Install Nginx web server (w/ Puppet)
exec {'Install nginx':
  command  => 'sudo apt-get -y update && sudo apt-get -y install nginx && sudo echo "Holberton School" > /var/www/html/index.html && new_string="\\\trewrite ^/redirect_me https://www.youtube.com/ permanent;" && sudo sed -i "30i $new_string" /etc/nginx/sites-available/default && sudo service nginx start',
  provider => shell,
    }
