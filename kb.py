from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton,
    ReplyKeyboardMarkup, ReplyKeyboardRemove
    )


menu = [
    [InlineKeyboardButton(text="📝 Генерировать текст", callback_data="generate_text"),
        InlineKeyboardButton(text="🖼 Генерировать картинку", callback_data="generate_image")],
    [InlineKeyboardButton(text="💳 Купить токены", callback_data="buy_tokens"),
        InlineKeyboardButton(text="💰 Баланс", callback_data="balance")],
    [InlineKeyboardButton(text="💎 Партнерка", callback_data="ref"),
        InlineKeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]

menu_test = [
    [InlineKeyboardButton(text="📝 Генерировать текст", callback_data="generate_text")],
    [InlineKeyboardButton(text="🖼 Генерировать картинку", callback_data="generate_image")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu_test)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀ Выйти в меню", callback_data="menu")]])
