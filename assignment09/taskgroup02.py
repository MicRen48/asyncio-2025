import asyncio

async def task(value):
    # sleep to simulate waiting
    await asyncio.sleep(1)
    # return value
    return value * 100

async def main():
    # create task group
    async with asyncio.TaskGroup() as group:
        # create and issue tasks
        tasks = [group.create_task(task(i)) for i in range(1,10)]

    # wait for all tasks to complete...
    # report all results
    for t in tasks:
        print(t.result())
asyncio.run(main())