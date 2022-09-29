import aiohttp
import asyncio
import time
from tqdm import tqdm

start_time = time.time()


async def main(url):

    async with aiohttp.ClientSession() as session:

        for i in tqdm(range(10)):
            url = url
            async with session.get(url) as resp:
                data = await resp.text()


asyncio.run(main(input("Введите URL адрес: ")))
print("--- %s seconds ---" % (time.time() - start_time))