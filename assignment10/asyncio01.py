# example of using an asyncio queue
from random import random
import asyncio

async def producer(queue):
    for i in range(10):
        value = 1
        sleeptime = random()
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        print(f"> Producer {value}")
        await queue.put(value)
    await queue.put(None)  # signal that we're done
    print("> Producer done")
async def consumer(queue):
    while True:
        try:
            iteam = queue.get_nowait()
        except asyncio.QueueEmpty:
            print(' Consumer: got nothing, waiting...')
            await asyncio.sleep(0.5)
            continue
        if iteam is None:
            break
        print(f'\t> Consumer got{iteam}')
    print('> Consumer done')   