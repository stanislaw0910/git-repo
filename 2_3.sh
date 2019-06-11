sudo /etc/init.d/mysql start
sudo pip3 install Django==2.0.0
mysql -uroot -e "CREATE DATABASE IF NOT EXISTS stepic_web;"
mysql -uroot -e "GRANT ALL ON stepic_web.* TO 'root'@'localhost';"
