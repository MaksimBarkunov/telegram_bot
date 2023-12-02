from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
# from aiogram.types.input_media import InputMediaPhoto 
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
token = "6317251238:AAEzvLGWpQNP100uNckktxChfQdIqYjThG0"
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands = ["start"])
async def start(msg:types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton("/обувь")
    b2 = KeyboardButton("/верхняя_одежда")
    b3 = KeyboardButton("/нижняя_одежда")
    b4 = KeyboardButton("/костюм")
    b5 = KeyboardButton("/пальто")
    b6 = KeyboardButton("/info")
    keyboard.add(b1,b2,b3,b4,b5,b6)
    await msg.reply("Здравствуйте, меня зовут бот «YoungTEA», я умею отвечать на популярные запросы пользователей и предоставлять каталог одежды по категориям.", reply_markup=keyboard)


@dp.message_handler(commands = ["обувь"])
async def shoes (msg:types.Message):
    p1 = "Ботинки мужские\n Цена: 3500"
    photo1 = open("python\READY project/bot__tellegramm\img\обувь\ботинки муж.jpg","br")
    await bot.send_photo(msg.from_user.id,photo1,caption=p1)
    photo1.close()
    p2 = "Туфли женские\nЦена: 2600"
    photo2 = open("python\READY project/bot__tellegramm\img\обувь\лоферы жен.jpg","br")
    await bot.send_photo(msg.from_user.id,photo2,caption=p2)
    photo2.close()
    p3 = "Лоферы женские\nЦена: 2100"
    photo3 = open("python\READY project/bot__tellegramm\img\обувь\туфли жен.jpg","br")
    await bot.send_photo(msg.from_user.id,photo3,caption=p3)
    photo3.close()



@dp.message_handler(commands = ["верхняя_одежда"])
async def outerwear (msg:types.Message):
    f1 = "Рубашка\nЦена: 1500"
    photo1 = open("python\READY project/bot__tellegramm\img\верхняя одежда\жилет.jpg","br")
    await bot.send_photo(msg.from_user.id,photo1,caption=f1)
    photo1.close()
    f2 = "жилет мужской\nЦена: 2400"
    photo2 = open("python\READY project/bot__tellegramm\img\верхняя одежда\рубашка.jpg","br")
    await bot.send_photo(msg.from_user.id,photo2,caption=f2)
    photo2.close()
    f3 = "свитер мужской\nЦена: 2400"
    photo3 = open("python\READY project/bot__tellegramm\img\верхняя одежда\свитер муж.jpg","br")
    await bot.send_photo(msg.from_user.id,photo3,caption=f3)
    photo3.close()


@dp.message_handler(commands = ["нижняя_одежда"])
async def underwear (msg:types.Message):
    h1 = "Брюки\nЦена: 2400"
    photo1 = open("python\READY project/bot__tellegramm\img\нижняя одежда\брюки муж.jpg","br")
    await bot.send_photo(msg.from_user.id,photo1,caption=h1)
    photo1.close()
    h2 = "Юбка\nЦена: 1800"
    photo2 = open("python\READY project/bot__tellegramm\img\нижняя одежда\шорты.jpg","br")
    await bot.send_photo(msg.from_user.id,photo2,caption=h2)
    photo2.close()
    h3 = "Шорты утепленные\nЦена: 1600"
    photo3 = open("python\READY project/bot__tellegramm\img\нижняя одежда\юбка.jpg","br")
    await bot.send_photo(msg.from_user.id,photo3,caption=h3)
    photo3.close()


@dp.message_handler(commands = ["костюм"])
async def suit (msg:types.Message):
    g1 = "Костюм мужской\nЦена: 5800"
    photo1 = open("python\READY project/bot__tellegramm\img\костюм\костюм муж.jpg","br")
    await bot.send_photo(msg.from_user.id,photo1,caption=g1)
    photo1.close()
    g2 = "Костюм женский\n Цена: 6000"
    photo2 = open("python\READY project/bot__tellegramm\img\костюм\костюм.jpg","br")
    await bot.send_photo(msg.from_user.id,photo2,caption=g2)
    photo2.close()
    g3 = "Платье\nЦена: 1900"
    photo3 = open("python\READY project/bot__tellegramm\img\костюм\платье.jpg","br")
    await bot.send_photo(msg.from_user.id,photo3,caption=g3)
    photo3.close()



@dp.message_handler(commands = ["пальто"])
async def coat (msg:types.Message):
    t1 = "Пальто мужское\nЦена: 4900"
    photo1 = open("python\READY project/bot__tellegramm\img\пальто\кардиган.jpg","br")
    await bot.send_photo(msg.from_user.id,photo1,caption=t1)
    photo1.close()
    t1 = "Пальто женское\nЦена: 6300"
    photo2 = open("python\READY project/bot__tellegramm\img\пальто\пальто муж.jpg","br")
    await bot.send_photo(msg.from_user.id,photo2,caption=t1)
    photo2.close()
    t3 = "Кардиган\nЦена: 2300"
    photo3 = open("python\READY project/bot__tellegramm\img\пальто\пальто.jpg","br")
    await bot.send_photo(msg.from_user.id,photo3,caption=t3)
    photo3.close()


@dp.message_handler(commands = ["info"])
async def info(msg:types.Message):
    await msg.reply("Бренд YoungTEA основан в 2017 году в городе Санкт-Петербург. Наша миссия — показать, что гардероб молодежи может состоять не только из худи и кроссовок. Все модели бренда передают эстетику тихого осеннего вечера с чашкой чая и книгой в руках.")
    

executor.start_polling(dp)