import asyncio
import json
import logging
import aiohttp

from config import setting
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

bot = Bot(setting.bot_token)
dp = Dispatcher()


async def get_giff_url(session, text, url):
    params = {'force': text}
    async with session.get(url) as response:
        image_resp = await response.text()
        image_link = json.loads(image_resp)['image']
        return image_link


async def get_gif_arr():
    gifs: {str: types.InlineQuery} = dict()
    predict = ['yes', 'no', 'maybe']
    url = 'https://yesno.wtf/api'
    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            for cur_text in predict:
                giff_url: str = await get_giff_url(session, cur_text, url)
                giff_id = giff_url.split('/')[-1].split('.')[0]
                gifs[cur_text] = types.InlineQueryResultGif(
                    id=giff_id,
                    gif_url=giff_url,
                    thumbnail_url=giff_url
                )
    return gifs


@dp.inline_query()
async def any_inline_query(inline_query: types.InlineQuery):
    gifs = await get_gif_arr()
    if gifs:
        gifs_link = list(gifs.values())
        await inline_query.answer(results=gifs_link)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
