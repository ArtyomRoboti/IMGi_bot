import sqlite3

conn = sqlite3.connect('../database.db')
cursor = conn.cursor()
cursor.execute('PRAGMA foreign_keys=ON')
conn.commit()


# Создание таблицы для хранения настроек генерации изображений
def create_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Settings(
        style_img TEXT DEFAULT "DEFAULT",
        style_shown TEXT DEFAULT "Стандартный",
        negative_prompt TEXT DEFAULT "Нет",
        width INT DEFAULT 1024,
        height INT DEFAULT 1024,
        current_size TEXT DEFAULT "1:1",
        id_user INT PRIMARY KEY,
        FOREIGN KEY (id_user) REFERENCES Users(id_user)
    );
    ''')
    conn.commit()

# Получить данные настройки запроса для пользователя
def get_set_user(id_user):
    cursor.execute('SELECT * FROM Settings WHERE id_user = ?', (id_user,))
    conn.commit()
    data: list = cursor.fetchall()
    return data

# Добавление ID пользователя при его регистрации
def create_user_id(id_tg):
    cursor.execute('INSERT INTO Settings (id_user) VALUES (?)', (id_tg,))
    conn.commit()


# Установить стиль генерации для конкретного пользователя
def set_style_user(id_user, style, style_show):
    cursor.execute('UPDATE Settings SET style_img = ?, style_shown = ?  WHERE id_user = ?',
                   (style, style_show, id_user))
    conn.commit()

# Уствновить негативный промпт для конретного пользователя
def set_negative_prompt(id_user, np):
    cursor.execute('UPDATE Settings SET negative_prompt = ? WHERE id_user = ?', (np, id_user))
    conn.commit()

# Установить размер изображения
def set_size_image(id_user, width, height, current_size):
    cursor.execute('UPDATE Settings SET width = ?, height = ?, current_size = ? WHERE id_user = ?',
                   (width, height, current_size, id_user))
    conn.commit()

