## Postgresql

    sudo apt-get install postgresql postgresql-contrib

###creating cluster

    pg_createcluster 9.3 main --start


### Remote access

    vim /etc/postgresql/9.3/main/pg_hba.conf

    host all all 0.0.0.0/0 trust


    vim /etc/postgresql/9.3/main/postgresql.conf
    listen_addresses = '*'


###Change password to postgres user

    passwd postgres
    sudo -s -u postgres
    psql
    \password postgres


###Restart server

    service postgresql restart


###Django connection

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'c4a',                      # Or path to database file if using sqlite3.
            'USER': 'chatuser',
            'PASSWORD': 'pasfas',
            'HOST': 'localhost',             
            'PORT': '',                      # Set to empty string for default.
        }
    }



