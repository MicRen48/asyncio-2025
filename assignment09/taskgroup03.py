import asyncio

async def task():
    print('Hello from corroutine 1')
    await asyncio.sleep(1)

async def task2():
    print('Hello from corroutine 2')
    await asyncio.sleep(0.5)
    raise Exception('Something bad happened')

async def task3():
    print('Hello from corroutine 2')
    await asyncio.sleep(1)

async def main():
    try:
        # create task group
        async with asyncio.TaskGroup() as group:
            # run first task
            t1 = group.create_task(task())
            # run second task
            t2 = group.create_task(task2())
            # run third task
            t3 = group.create_task(task3())
    except:
        pass
    print(f'Task 1 done: {t1.done()}, cancelled: {t1.cancelled()}')
    print(f'Task 2 done: {t2.done()}, cancelled: {t2.cancelled()}')
    print(f'Task 3 done: {t3.done()}, cancelled: {t3.cancelled()}')
    
asyncio.run(main())    
  