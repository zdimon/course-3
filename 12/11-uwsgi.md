##UWSGI

    apt-get install uwsgi uwsgi-plugin-python uwsgi-plugin-python
    
    
## Modes

Command

    uwsgi --module myapp --socket :3030 --stats /tmp/stats.socket
    
INI        

###Create ini file

    sudo nano /etc/uwsgi/apps-enabled/site.ini

    [uwsgi]
    thread          = 3
    master          = true
    processes       = 2
    
    module          = blog.wsgi
    
    
    chdir           = /home/webmaster/blog
    
    
    http            = 127.0.0.1:8001
    socket          = /tmp/blog.sock



    home            = /home/webmaster/venv








    plugins         = python3
    buffer-size     = 32768





#uid = webmaster
#gid = webmaster
# socket          = /tmp/blog.sock
#logto           = /home/zdimon/www/course-2/blog.uwsgi.log

    

###Restarting uwsgi server

    sudo service uwsgi restart

###Create vhost block in nginx file


    server {
        listen      80;
        server_name blog.local.com;
        access_log  /home/zdimon/www/course-2/blog/nginx.log;
        location / {
               uwsgi_pass      unix:///tmp/blog.sock;
               include         uwsgi_params;
               #proxy_pass http://127.0.0.1:8888;
        }
        location /static {
            alias /home/zdimon/www/course-2/blog/static;
        }
       location /media {                                                                                                                                                           
            alias /home/zdimon/www/course-2/blog/media;                                                                                                                                   
        }   
    }    

##Statistic

    https://github.com/xrmx/uwsgitop
    
    pip install uwsgitop


    --stats 127.0.0.1:1717
    --stats /tmp/statsock

    uwsgitop /tmp/stat.sock
