# where-is-my-card
Аналог приложения "Кошелек", но лучше и в телеграме.


## Запуск

Перед командами запуска создайте файл `docker/.dockerenv` по примеру `docker/.dockerenv.example`

А теперь команды:
1. сборка + запуск: `make launch`
2. стоп + сборка + запуск: `make reload`
3. стоп + запуск: `make restart`
4. сборка: `make build`
5. запуск: `make up`
6. стоп: `make down`