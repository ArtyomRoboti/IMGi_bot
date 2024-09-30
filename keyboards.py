from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# Клавиатура с основными кнопками
kb_main_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Генерация изображения👨‍🎨'), KeyboardButton(text='Настройки генерации⚙️'), ],
    [KeyboardButton(text='Просмотр изображения🖼'), KeyboardButton(text='Рейтинг изображений🥇')],
    [KeyboardButton(text='Оценить изображения🗳'), KeyboardButton(text='Сообщеть об ошибке❌')],
    [KeyboardButton(text='Информация о ботеℹ️')],
], resize_keyboard=True)

# Клавиатура для выбора настройки генерации
kb_settings = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Стиль✨')],
    [KeyboardButton(text='Негативный промт🚫')],
    [KeyboardButton(text='Размер изображения🔲')],
    [KeyboardButton(text='Назад🔙')]
], resize_keyboard=True, one_time_keyboard=True)

# Клавиатура для работы со сгенерированной фотографией
kb_save_img = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сохранить✅', callback_data='save'),
     InlineKeyboardButton(text='Отменить🚫', callback_data='cancel')],
    [InlineKeyboardButton(text='Сгенерировать заново🔁', callback_data='repeat')],
], resize_keyboard=True)

# Клавиатура для выбора стиля генерации
kb_set_style = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Стандартный', callback_data='DEFAULT'), InlineKeyboardButton(text='Реалистичный', callback_data='UHD')],
    [InlineKeyboardButton(text='Аниме', callback_data='ANIME'), InlineKeyboardButton(text='Кандинский', callback_data='KANDINSKY')],
    [InlineKeyboardButton(text='Назад', callback_data='back')]
], resize_keyboard=True)

# Клавиатура для выхода из настройки негативного промта
kb_cancel_np = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отмена', callback_data='cancel_np')]
], resize_keyboard=True)

# Клавиатура для выбора размера изображения при генерации которое будет
kb_set_size = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1️⃣6️⃣:9️⃣', callback_data='16:9'), InlineKeyboardButton(text='9️⃣:1️⃣6️⃣', callback_data='9:16')],
    [InlineKeyboardButton(text='3️⃣:2️⃣', callback_data='3:2'), InlineKeyboardButton(text='2️⃣:3️⃣', callback_data='2:3')],
    [InlineKeyboardButton(text='Назад', callback_data='back')]
], resize_keyboard=True)
