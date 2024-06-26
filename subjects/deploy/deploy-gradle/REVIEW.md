## Рецензия

### Дополнительная информация

<img src="../../../resources/code-review.png" alt="code-review.png" width="250"/>

Рецензия - это проверка проекта другого учащегося. Перед тем, как приступить к рецензированию, ознакомьтесь с правилами проведения рецензии.

**Правила рецензии:**

- Проверять только выполненную работу.
- Следовать указаниям критериев оценки.
- Если проект учащегося соответствует критерию, то ставьте 1.
- Если проект учащегося не соответствует критерию, то ставьте 0.

### Критерий оценки #1

GitHub ссылка рабочая и ведет на репозиторий с выполненным заданием.

Если это не так, то ставьте оценку 0 и заканчивайте проверку.

### Критерий оценки #2

1. В репозитории существует директория `deploy-php`.

2. В ней присутствуют обязательные файлы:

- Dockefile
- docker-compose.yml
- deploy-php.conf

3. Dockefile использует `ubuntu:18.04` как основной образ.

4. В docker-compose.yml описан только один сервис `winter`.

5. В docker-compose.yml под сервисом `winter` нет директивы `image`, а используется директива `build`.

6. Сборка образа проходит успешно.

```bash
docker-compose build
```

7. Запуск проекта проходит успешно.

```bash
docker-compose up -d
```

8. Зайдите на `http://localhost/`, страница открывается успешно.
9. Проверьте работоспособность сайта, пройдитесь по разным доступным страницам.

### Критерий оценки #3

1. В репозитории существует директория `deploy-python`.

2. В ней присутствуют обязательные файлы:

- Dockefile
- docker-compose.yml
- deploy-python.conf

3. Dockefile использует `ubuntu:18.04` как основной образ.

4. В docker-compose.yml описаны только два сервиса `demo` и `nginx`.

5. В docker-compose.yml под сервисом `demo` нет директивы `image`, а используется директива `build`.

6. Сборка образа проходит успешно.

```bash
docker-compose build
```

7. Запуск проекта проходит успешно.

```bash
docker-compose up -d
```

8. Зайдите на `http://localhost/`, страница открывается успешно.
9. Проверьте работоспособность сайта, пройдитесь по разным доступным страницам.

### Критерий оценки #4

1. В репозитории существует директория `deploy-maven`.

2. В ней присутствуют обязательные файлы:

- Dockefile
- docker-compose.yml
- deploy-maven.conf

3. Dockefile использует `ubuntu:18.04` как основной образ.

4. В docker-compose.yml описаны только два сервиса `app` и `nginx`.

5. В docker-compose.yml под сервисом `app` нет директивы `image`, а используется директива `build`.

6. Сборка образа проходит успешно.

```bash
docker-compose build
```

7. Запуск проекта проходит успешно.

```bash
docker-compose up -d
```

8. Зайдите на `http://localhost/`, страница открывается успешно.
9. Проверьте работоспособность сайта, пройдитесь по разным доступным страницам.

### Критерий оценки #5

1. В репозитории существует директория `deploy-gradle`.

2. В ней присутствуют обязательные файлы:

- Dockefile
- docker-compose.yml
- deploy-gradle.conf

3. Dockefile использует `ubuntu:18.04` как основной образ.

4. В docker-compose.yml описаны только два сервиса `app` и `nginx`.

5. В docker-compose.yml под сервисом `app` нет директивы `image`, а используется директива `build`.

6. Сборка образа проходит успешно.

```bash
docker-compose build
```

7. Запуск проекта проходит успешно.

```bash
docker-compose up -d
```

8. Зайдите на `http://localhost/`, страница открывается успешно.
9. Проверьте работоспособность сайта, пройдитесь по разным доступным страницам.
