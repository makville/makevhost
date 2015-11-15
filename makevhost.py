import os

domain = raw_input('Enter domain name: ')
path = '/var/www/html/' + domain + '/'
public_html = path + 'public_html/'
index = path + 'public_html/index.php'
#Create the directories
if not os.path.exists(path):
	os.makedirs(path)
	os.makedirs(public_html)
#Grant permissions
os.system("chown -R $USER:$USER " + public_html)
#Create a demo index.php file
with open(index, 'w') as index_file:
	index_file.write('<?php' + "\n")
	index_file.write("\t" + 'echo "' + domain + ' is working";' + "\n")
	index_file.write('?>')
#Create the virtual host file
vhost_conf = '/etc/apache2/sites-available/' + domain + '.conf'
with open(vhost_conf, 'w') as conf_file:
	conf_file.write('<VirtualHost *:80>' + "\n")
	conf_file.write("\t" + 'ServerName ' + domain + "\n")
	conf_file.write("\t" + 'ServerAlias www.' + domain + "\n")
	conf_file.write("\t" + 'ServerAdmin admin@' + domain + "\n")
	conf_file.write("\t" + 'DocumentRoot ' + public_html + "\n\n")
	conf_file.write("\t" + 'ErrorLog ${APACHE_LOG_DIR}/error.log' + "\n")
	conf_file.write("\t" + 'CustomLog ${APACHE_LOG_DIR}/access.log combined' + "\n")
	conf_file.write('</VirtualHost>')
	conf_file.write('' + "\n")
	conf_file.write('<Directory "' + public_html + '">' + "\n")
	conf_file.write("\t" + 'AllowOverride All' + "\n")
	conf_file.write('</Directory>')
#Enable the virtual host file 
os.system('a2ensite ' + domain + '.conf') 
os.system('service apache2 reload')
																																												
