Anders-Motors - ремонт экстремальных видов техники.

Коммерческая разработка одностраничного сайта на Django с применением Bootstrap и API Telegram.

Основной функционал сайта - форма сбора контактных данных, а также уведомление владельца о получении новых контактов через телеграм-бота (pyTelegramBotAPI).

Стек используемых технелогий: Django, Bootstrap, SQLite.

Для запуска проекта необходимо:
1. Создать директорию /config/config.py в корневой папке проекта и прописать переменные:
bot_token = 'Токен_вашего_бота'
my_id = 'ID_вашего_аккаунта'

Но лучше настроить переменные окружения .env, либо добавить эту директорию в .gitignore.

2. Установить зависимости requirements в вашем виртуальном окружении pip install -r requirements.
