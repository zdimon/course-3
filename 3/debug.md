#Отладка


## Pdb

Python имеет встроенный отладчик: модуль pdb. 



## Ipdb

    pip install ipython ipdb
    import ipdb; ipdb.set_trace()



Но гораздо лучше в Django использовать модуль django-extensions, который добавляет очень полезную команду runserver_plus. 

Ещё один хороший модуль, на этот раз для Django: django-pdb. Он позволяет запускать отладчик при наличии соответствующего GET-параметра в запросе (например: http://127.0.0.1:8000/app/view?ipdb) 

