# deploy-python

Python - это интерпретируемый язык программирования. Популярен в backend разработке и анализе данных.

Пакетный менеджер Python это [pip](https://packaging.python.org/en/latest/key_projects/#pip). Зависимости проекта описываются в файле requirements.txt ([пример файла](https://raw.githubusercontent.com/bndr/pipreqs/master/requirements.txt)).

### Полезное

- [Compose and Django](https://docs.docker.com/samples/django/)

### Задание

1. Вся работа должна выполняться в GitHub Classroom в папке `deploy-python`.
2. Написать Dockerfile, который:

   - использует за основу образ `ubuntu:18.04`;
   - клонирует репозиторий [demo](https://github.com/django-ve/django-helloworld);
   - устанавливает зависимости: Python3, pip, и т.д.
   - устанавливает зависимости проекта с помощью пакетного менеджера pip.
   - 💡 посмотрите содержимое файлов в директории `helloworld`, особое внимание обратите на `settings.py`;
   - проводит подготовку проекта: создание конфигурации, накатывание миграции и наполнение базы.
   - запускает проект в директиве `CMD` или `ENTRYPOINT`.

3. Написать `docker-compose.yml`, который:

   - имеет два сервиса `nginx` и `demo`;
   - сервис `demo` собирает сборку из текущей директории (прим. `build`);
   - сервис `demo` имеет имя контейнера `deploy-python-demo`;
   - сервис `nginx` использует образ `nginx:mainline`.
   - сервис `nginx` перенаправляет запрос с хостового порта 80 на 80 порт контейнера;
   - сервис `nginx` монтирует `deploy-python.conf` внутрь контейнера.
   - сервис `nginx` зависит от `demo`;
   - сервис `nginx` имеет имя контейнера `deploy-python-nginx`;
   - оба сервиса перезапускаются в случае провала;

4. Создать конфигурационный файл `deploy-python.conf` для nginx, который:

   - слушает 80 порт;
   - перенаправляет запросы на сервис `demo`;

5. Запустить docker-compose.yml и проверить работает ли в браузере [http://localhost/admin](http://localhost/admin).
6. Запушить в гит: `Dockerfile`, `docker-compose.yml`, `deploy-python.conf`.

---

### Ответ

- [Dockerfile](Dockerfile)
- [docker-compose.yml](docker-compose.yml)
- [deploy-python.conf](deploy-python.conf)
