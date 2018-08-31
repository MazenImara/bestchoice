configuration for apache2:

<VirtualHost *:80>
    ServerAdmin admin@bestchoice.live
    ServerName bestchoice.live
    ServerAlias www.bestchoice.live
    WSGIScriptAlias / /var/www/bestchoice/bestchoice/django.wsgi
    <Directory /var/www/bestchoice/bestchoice>
        Order deny,allow
        Allow from all
    </Directory>

    ErrorLog /var/log/apache2/error.log
    LogLevel warn

    CustomLog /var/log/apache2/access.log combined

    Alias /static/ /var/www/bestchoice/bestchoice/static/


</VirtualHost>

<VirtualHost *:80>
    ServerAdmin admin@bestchoice.live
    ServerName uropenn.bestchoice.live
    ServerAlias www.bestchoice.live
    WSGIScriptAlias / /var/www/bestchoice/bestchoice/django.wsgi
    <Directory /var/www/bestchoice/bestchoice>
        Order deny,allow
        Allow from all
    </Directory>
    Alias /static/ /var/www/bestchoice/bestchoice/static/
</VirtualHost>