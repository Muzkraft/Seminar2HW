from aiogram.utils import executor
from handlers import dp


async def on_startup(_):
    print('Работаем!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
