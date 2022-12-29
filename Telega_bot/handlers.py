import random
from aiogram.utils.markdown import text
from aiogram.types import Message
from bot_config import dp
import text
import game
from keyboard import kb_new, kb_stop
from wiki import get_wiki


@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.answer(text=f'{message.from_user.first_name}'
                              f'{text.greeting}', reply_markup=kb_new)


@dp.message_handler(commands=['wiki'])
async def wiki(message: Message):
    await message.answer(text='Напиши любое слово, и я расскажу тебе что-нибудь о нем.')
    await message.reply(get_wiki(message.text[6:]))


@dp.message_handler(commands=['new_game'])
async def start_new_game(message: Message):
    if game.check_game_start():
        game.set_total_to_max()
    else:
        game.new_game()
    if game.check_game_start():
        toss = random.choice([True, False])
        if toss:
            await player_turn(message)
        else:
            await bot_turn(message)


@dp.message_handler(commands=['stop_game'])
async def stop_game(message: Message):
    game.new_game()
    await message.reply('Игра окончена!', reply_markup=kb_new)


@dp.message_handler(commands=['set_total'])
async def set_total_candies(message: Message):
    if not game.check_game_start():
        max_total = message.text.split()
        if len(max_total) > 1 and max_total[1].isdigit():
            game.set_max_total(int(max_total[1]))
            await message.reply(text=f'На столе стало лежать {max_total[1]} конфет.')
        else:
            await message.reply(text='Этой командой можно изменить максимальное количество конфет. '
                                     'Для этого напиши /set_total и целое число конфет.')
    else:
        await message.reply(text='Эту настройку можно совершить только по окончании игры.')


@dp.message_handler(commands=['set_level'])
async def set_level(message: Message):
    if not game.check_game_start():
        game.change_level()
        await message.reply(text=f'Уровень сложности {game.get_bot_level()}')
    else:
        await message.reply(text='Эту настройку можно совершить только по окончании игры.')


async def player_turn(message: Message):
    await message.answer(text=f'{message.from_user.first_name}, '
                              f'Твой ход. Сколько конфет возьмешь?', reply_markup=kb_stop)


@dp.message_handler(commands=['help'])
async def help(message: Message):
    await message.reply(text=f'{message.from_user.first_name}{text.help}')


@dp.message_handler()
async def take(message: Message):
    name = message.from_user.first_name
    if game.check_game_start():
        if message.text.isdigit():
            take = int(message.text)
            if (0 < take < 29) and take <= game.get_total():
                game.take_candies(take)
                if await check_win(message, take, 'player'):
                    return
                await message.answer(f'{name} взял {take} конфет и на столе осталось '
                                     f'{game.get_total()} конфет. Ходит бот...')
                await bot_turn(message)
            else:
                await message.answer('А попа не слипнется? Возьми от 1 до 28 конфет. ')
        else:
            pass


async def bot_turn(message):
    total = game.get_total()
    take = 1
    if game.get_bot_level() == 'Easy':
        if total <= 28:
            take = total
        else:
            take = random.randint(1, 28)
    else:
        if total <= 28:
            take = total
        else:
            var = (game.get_total() - 29) % 28
            take = var if var > 0 else random.randint(1, 28)
    game.take_candies(take)
    await message.answer(f'Бот взял {take} конфет и их осталось {game.get_total()}.', reply_markup=kb_stop)
    if await check_win(message, take, 'Бот'):
        return
    await player_turn(message)


async def check_win(message, take: int, player: str):
    if game.get_total() <= 0:
        if player == 'player':
            await message.answer(f'{message.from_user.first_name} взял {take} конфет и победил ботяру!')
        else:
            await message.answer(f'Ботяра взял {take} конфет и победил тебя, {message.from_user.first_name}'
                                 f'! Как тебе не стыдно!')
        game.new_game()
        return True
    else:
        return False