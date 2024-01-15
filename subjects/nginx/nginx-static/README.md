# nginx-static

Важной задачей веб-сервера является обслуживание файлов (например, изображений или статических HTML-страниц).

В этом уроке мы реализуем пример, где в зависимости от запроса файлы будут обслуживаться из разных директорий:

- `/var/www/example/web-site`, который содержит файлы HTML
- `/var/www/example/images`, содержащий изображения.

> 🕹 Запускайте следующие шаги на своем компьютере с установленным `nginx`

Это потребует редактирования файла конфигурации и настройки блока `server` внутри блока `http` с двумя блоками `location`.

1. Сначала создайте директорию `/var/www/example/web-site` и поместите в него файл [index.html](https://stepik.org/media/attachments/lesson/686238/index.html).
2. Создайте директорию `/var/www/example/images` и поместите в него изображения из [архива](https://stepik.org/media/attachments/lesson/686238/cats.zip).
3. Далее перенастроим дефолтные настройки сервера, удалим файл `/etc/nginx/conf.d/default.conf`.
4. Создадим новый конфигурационный файл `/etc/nginx/conf.d/example.conf`.
5. Откроем файл и начнем с `server` блока.

```nginx
server {

}
```

Как правило, файл конфигурации может включать в себя несколько `server` блоков, отличающихся [портами](http://nginx.org/en/docs/http/request_processing.html), которые они [прослушивают](http://nginx.org/en/docs/http/ngx_http_core_module.html#listen), и [именами серверов](http://nginx.org/en/docs/http/server_names.html). Как только nginx решает, какой `server` обрабатывает запрос, он проверяет URI, указанный в заголовке запроса, на соответствие параметрам директив `location`, определенных внутри блока `server`.

6. Добавьте следующий блок `location` в блок `server`:

```nginx
location / {
    root /var/www/example/web-site;
}
```

Блок `location` указывает префикс `/` для сравнения с URI из запроса. Для совпадающих запросов к пути, указанному в директиве `root`, то есть к `/var/www/example/web-site`, будет добавлен URI, чтобы сформировать путь к запрашиваемому файлу в локальной файловой системе.

Если есть несколько совпадающих блоков `location`, nginx выбирает блок с самым длинным префиксом.
Вышеприведенный блок `location` предоставляет самый короткий префикс длины один, поэтому этот блок будет использоваться только в том случае, если все остальные блоки `location` не обеспечивают совпадения.

7. Затем добавьте второй блок `location`:

```nginx
location /images/ {
    root /var/www/example;
}
```

Это будет соответствовать запросам, начинающиеся с `/images/` (блок `location` `/` также соответствует таким запросам, но имеет более короткий префикс).

В результате конфигурация блока `server` должна выглядеть так:

```nginx
server {
    location / {
        root /var/www/example/web-site;
    }

    location /images/ {
        root /var/www/example;
    }
}
```

Это уже рабочая конфигурация сервера, который прослушивает дефолтный порт 80. Сайт доступен на локальной машине по адресу `http://localhost/`.

В ответ на запросы с URI, начинающиеся с `/images/`, сервер будет отправлять файлы из каталога `/var/www/example/images`. Например, в ответ на запрос `http://localhost/images/example.png` nginx отправит файл `/var/www/example/images/example.png`. Если такого файла не существует, nginx отправит ответ с указанием ошибки 404.

Запросы с URI, не начинающиеся с `/images/`, будут сопоставлены с каталогом `/var/www/example/web-site`. Например, в ответ на запрос `http://localhost/some/example.html` nginx отправит файл `/data/www/some/example.html`.

Чтобы применить новую конфигурацию, запустите nginx, если он еще не запущен, или отправьте сигнал перезагрузки главному процессу nginx, выполнив:

```bash
nginx -s reload
# или
systemctl reload nginx
# или
service nginx reload
```

> Если что-то не работает должным образом, вы можете попытаться выяснить причину в файлах `access.log`
> и `error.log` в каталоге `/var/log/nginx`.

### Полезные ссылки

- [Создание server блоков с разными портами](http://nginx.org/en/docs/http/request_processing.html)
- [Настройка server блока: listen](http://nginx.org/en/docs/http/ngx_http_core_module.html#listen)
- [Настройка server блока: имя сервера](http://nginx.org/en/docs/http/server_names.html)
