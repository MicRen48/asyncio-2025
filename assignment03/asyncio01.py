# check the type of a corutine
import asyncio

async def custom_coro():
    await asyncio.sleep(1)

coro = custom_coro()

print(type(coro))