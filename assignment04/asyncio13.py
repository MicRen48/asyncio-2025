# all tasks
import asyncio

async def dummy():
    await asyncio.sleep(2)

async def main():
    t1 = asyncio.create_task(dummy(), name="Task A")
    t2 = asyncio.create_task(dummy(), name="Task B")

    await asyncio.sleep(0.1) # ให้เวลา Tasks เริ่มทำงาน

    all_tasks = asyncio.all_tasks()
    print("Task ทั้งหมดใน loop:")
    for t in all_tasks:
        print("_-", t.get_name())

    # ต้องรอให้ tasks จบด้วย มิฉะนั้น loop จะปิดก่อน
    await t1
    await t2

asyncio.run(main())