# Deploy 

## SSH

    git add --all
    git commit -m 'Auto'
    git push
    ssh -t zdimon@quizer.com.ua "cd gamehub; git pull"
    ssh -t zdimon@quizer.com.ua "cd gamehub; . ./ve/bin/activate;  pip install -r requirements.txt"
    ssh -t zdimon@quizer.com.ua "cd gamehub/dj; . ../ve/bin/activate;  ./manage.py migrate"
    ssh -t zdimon@quizer.com.ua "cd gamehub; npm install"

## Fabric

#fabfile.py

    # -*- coding: utf-8 -*-
    from fabric.api import *
    import os
    from contextlib import contextmanager as _contextmanager



    env.key_filename = [os.path.join(os.environ['HOME'], '.ssh', 'id_rsa.pub')]  # Локальный путь до файла с ключами
    env.user = 'webmaster'  # На сервере будем работать из под пользователя "zdimon"



    env.project_root = '/home/webmaster/wm_ve/wm'  # Путь до каталога проекта (на сервере)
    env.activate = 'source /home/webmaster/wm_ve/bin/activate'
    env.hosts = ['webmonstr.com']

    env.port =  22

    @_contextmanager
    def virtualenv():
        with cd(env.project_root):
            with prefix(env.activate):
                yield




    def deploy():
        with virtualenv():
            run('git pull') # Пуляемся из репозитория
            run('pip install -r requirements.txt') # ставим пакеты
            #run('bower install')
            run('./manage.py collectstatic --noinput') # Собираем статику
            #run('./manage.py sync_translation_fields --noinput') # Собираем статику
            run('./manage.py migrate')
            run('./manage.py load_page')
            run('./manage.py load_course')
            

### Run

    fab deploy




