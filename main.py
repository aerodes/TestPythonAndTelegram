import aiogram
import asyncio
import logging
import time
import emoji
import aioschedule
#from aiogram import Text
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.utils.keyboard import InlineKeyboardBuilder



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

#1132448356
@dp.message(Command("stas"))
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
    await message.answer(f"Отправим Стасу кубик?)", reply_markup=keyboard)

@dp.message(Command("den"))
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

@dp.message(lambda message: message.text == "Да")
async def cmd_dice(message: types.Message, bot: Bot):
    await bot.send_dice(chat_id=1132448356, emoji=DiceEmoji.DICE)

@dp.message(lambda message: message.text == "Нет")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!")

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message, bot: Bot):
    await bot.send_dice(chat_id=1132448356, emoji=DiceEmoji.DICE)

@dp.message(Command("inline_url"))
async def cmd_inline_url(message: types.Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="GitHub", url="https://github.com")
    )
    builder.row(types.InlineKeyboardButton(
        text="Оф. канал Telegram",
        url="tg://resolve?domain=telegram")
    )

    # Чтобы иметь возможность показать ID-кнопку,
    # У юзера должен быть False флаг has_private_forwards
    user_id = 385329543
    chat_info = await bot.get_chat(user_id)
    if not chat_info.has_private_forwards:
        builder.row(types.InlineKeyboardButton(
            text="Какой-то пользователь",
            url=f"tg://user?id={user_id}")
        )

    await message.answer(
        'Выберите ссылку',
        reply_markup=builder.as_markup(),
    )

# Запуск процесса поллинга новых апдейтов

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



