sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn1.conf   /etc/gunicorn.d/wsgi.example
sudo /etc/init.d/gunicorn restart
