import logging
from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

TOKEN = 5722239636:AAHLdaefsU1eImCSLQYaeR07uK3rU5IP9_k

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)
logging.basicConfig(level=logging.DEBUG)
@dp.message_handler(Text(equals="Андрей", ignore_case=True), state="*")
async def cmd_start(message: types.Message, state: FSMContext):
    media = types.InputFile('picture.jpg')
    info = '''
    <i>Информация о субъекте:</i>

    <code>Имя: Андрей
    <code>Фамилия: Мараховский
    <code>Отчество: Павлович
    <code>Профессия: Безработный
    '''

    await message.answer_photo(media)  # отвечаем на сообщение картинкой
    await message.answer(info)  # отвечаем на сообщение текстом


executor.start_polling(dp, skip_updates=True)