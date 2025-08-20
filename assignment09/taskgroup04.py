import asyncio

async def task1():
    await asyncio.sleep(1)
    print('Hello From coroutine 1')

async def task2():
    await asyncio.sleep(1)
    print('Hello From coroutine 2')

async def task3():
    await asyncio.sleep(1)
    print('Hello From coroutine 3')

async def main():
    async with asyncio.TaskGroup() as group:
        t1 = group.create_task(task1())
        t2 = group.create_task(task2())
        t3 = group.create_task(task3())
        await asyncio.sleep(0.5)  # Simulate some other work
        t2.cancel()  # Cancel task2

    print(f'Task 1 done: {t1.done()}, cancelled: {t1.cancelled()}')
    print(f'Task 2 done: {t2.done()}, cancelled: {t2.cancelled()}')
    print(f'Task 3 done: {t3.done()}, cancelled: {t3.cancelled()}')

asyncio.run(main())