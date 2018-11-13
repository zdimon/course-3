The __file__ variable contains the path to the file that Python is currently importing. 


When Python imports a module, it sets the __name__ variable to be a string containing the name of the module it is importing.



Модуль sys обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python.

sys.argv - список аргументов командной строки,
sys.exit([arg]) - выход из Python. 
sys.path - список путей поиска модулей.

Модуль os предоставляет множество функций для работы с операционной системой

os.environ - словарь переменных окружения. 

os.path - модуль, реализующий некоторые полезные функции на работы с путями.
os.path.split(path) - разбивает путь на кортеж (голова, хвост)
os.path.splitext(path) - разбивает путь на пару (root, ext),
os.path.basename(path) - базовое имя пути

if not os.path.exists(directory):
    os.makedirs(directory)


os.mkdir(path, mode=0o777, *, dir_fd=None) - создаёт директорию. 



filename = os.path.splitext(os.path.basename(__file__))[0]




