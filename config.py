from datetime import date

bot_create_date = date(year=2023, month=6, day=1) # ДАТА СОЗДАНИЯ БОТА
bot_version = "1.12" # ВЕРСИЯ БОТА

token = "" # ТОКЕН ОТ БОТА
path_to_database = r"database.db" # ПУТЬ К БАЗЕ ДАННЫХ
path_to_data_dir = r"data" # ПУТЬ К ПАПКЕ С ФАЙЛАМИ, КОТОРЫЕ БУДЕТ ГЕНЕРИРОВАТЬ БОТ
path_to_log_dir = r"logs" # ПУТЬ К ПАПКЕ С ЛОГАМИ
path_to_html_template = r"template.html" # ПУТЬ К ШАБЛОНУ HTML ДЛЯ ГЕНЕРАЦИИ ТАБЛИЦЫ С ПОЛЬЗОВАТЕЛЯМИ
admins = [] # ID АДМИНОВ
programmer= "@autor1" # НИК ПРОГРАММИСТА КОТОРЫЦ СОЗДАЛ БОТ
bot_owner = "@autor1" # НИК ВЛАДЕЛЬЦА БОТА
ad = "@autor1" # НИК АККАУНТА НА КОТОРЫЙ ПИСАТЬ ПО ПОВОДДУ РЕКЛАМЫ
customer_service = "@autor1" # НИК АККАУНТА СЛУЖБЫ ПОДДЕРЖКИ
check_subscribe = True # НУЖНО ЛИ ПРОВЕРЯТЬ ПОДПИСАН ЛИ ПОЛЬЗОВАТЕЛЬ НА КАНАЛЫ
channels = [
    {"link": "@pythonproga", "id": -1001733995580, "name": "Python Proga"},
    {"link": "https://t.me/pythonproga", "id": -1001733995580},
    {"link": "https://t.me/+9CVfdpYB4aExMWRi", "id": -1001733995580}
] # КАНАЛЫ НА КОТОРЫЕ ПОЛЬЗОВАТЕЛЬ ДОЛЖЕН БЫТЬ ПОДПИСАН
