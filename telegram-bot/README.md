# telegram-bot
В файле bot.py представлен простой телеграм бот который отправляет вам сообщение "Hello World!" на команду /start

### Задание:
- Создать бота в [@BotFather](https://t.me/BotFather) (/newbot)
- Получить в [@BotFather](https://t.me/BotFather) API ключ для вашего бота
- Написать Dockerfile, в котором будет запускаться bot.py, API ключ - переменная окружения TOKEN [(Что такое переменная окружения?)](https://ru.hexlet.io/courses/cli-basics/lessons/environment-variables/theory_unit)
- Передать API ключ в качестве аргумента при запуске контейнера
- Проверить работоспособность
### Подсказки:
- Для передачи ключа в качестве аргумента используйте ENV и ARG
- Для проверки работоспособности, отправьте /start вашему боту