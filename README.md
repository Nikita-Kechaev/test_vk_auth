# Инструкции по развертыванию тестового приложения test_VK_auth

1. В коревой директории создать файл .env
2. В .env файле обозначить следующие переменные:
    * DJANGO_SECRET_KEY=        # Can be generated here: <https://djecrety.ir/>
    * DJANGO_ALLOWED_HOSTS=     # hosts split by whitespace
    * DJANGO_DEBUG=             # 1 or 0
    * DB_NAME=
    * DB_USER=
    * DB_PASSWORD=
    * DB_PORT=
    * DB_HOST= # For use local database, set `host.docker.internal`

3. Создать приложение VK mini. Подробнее по ссылке <https://vk.com/dev>
4. Добавить в .env следующие переменные:
    * AUTH_VK_KEY= # id созданного приложения
    * AUTH_VK_SECRET= # secret_key созданного приложения
5. Выполнить команду sudo docker compose -f docker-compose.dev.yml up -d --build
6. Выполнить миграции в контейнере web:
    * sudo docker compose exec web python manage.py makemigrations
    * sudo docker compose exec web python manage.py migrate
7. Создать superuser:
    * sudo docker compose exec web python manage.py createsuperuser
8. Получить api-token для работы с приложением VK-mini перейдя по ссылке:

    * <https://oauth.vk.com/blank.html#access_token=vk1.a.W6PXFAILiPtmSVzoVlI6a6t_ELiDgVksQ3bSYdrIHjuJueWk7MsbtjFhlFrQKoBqZYTS3KMDAAC6FMxAFuD_pqJ_H-Bt_vI3gyk8VIy3HLxqZQ2bUg0BBeqk1jVnlWyF_sfM4fxUF19YYNQZYaL-oS3uZz8tJ-h75TEstxqqzlfukcz8dWheWa10dceyPmVt&expires_in=86400&user_id=XXXXXX> где XXXXXX == AUTH_VK_KEY
    * Запомнить токен для послдющих post запросов в postman или thunder

9. В admin панеле создать Applications:
    * запомнить сгенерированный Client id для последующих post запросов в postman или thunder
    * user = 1 (admin)
    * client type = public
    * Authorization grant type = Client credentials

10. Создать post запрос по ссылке <http://127.0.0.1:8000/api/auth/convert-token>
    * В теле запроса указать след. информацию:
    * {
        "grant-type": "convert_token",
        "client_id" : "# Client_id из 9 п.",
        "token": "# api - token полученный в 8п.",
        "backend": "vk-oauth2"
    }
11. Полученный access_token используем в качестве Bearer токена.
12. Поздавляю, аутентификация через VK пройдена )))
