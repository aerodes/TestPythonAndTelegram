import asyncio
import logging
import time
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6349801232:AAHHgfoc0-rSmFOIWAZnodOFOt2qUEpSt98")
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("huisosite")

# Хэндлер на команду /test2
@dp.message(Command("test2"))
async def cmd_test2(message: types.Message):
    await message.answer("Krasava")

@dp.message(Command("star"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text=f"Да")],
        [types.KeyboardButton(text=f"Нет")]

    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="УВЕРЕН??"
    )
    await message.answer(f"Отправим Денису кубик?)", reply_markup=keyboard) 

@dp.message(lambda message: message.text == "Да")    #Это позже перенесу в отдельные кнопки и еще до этого добалю выбор 
async def cmd_dice(message: types.Message, bot: Bot): #надо только узнать как без команды начинать взаимодействие, чтобы сразу было меню с командами
    await bot.send_dice(chat_id=1132448356, emoji=DiceEmoji.DICE)

@dp.message(lambda message: message.text == "Нет")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!")

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message, bot: Bot):
    await bot.send_dice(chat_id=450998839, emoji=DiceEmoji.DICE)   ##Пока тут айпи Стаса, может придумаем чот

# Запуск процесса поллинга новых апдейтов

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



