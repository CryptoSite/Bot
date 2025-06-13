import os
from aiogram import Bot, Dispatcher, executor, types

# Читаем токен из переменных окружения
API_TOKEN = os.getenv("7261988531:AAG2x6KgxklJuI96bzk2hUR68mJicwFC6_0")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я работаю на Railway! 🚄")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
