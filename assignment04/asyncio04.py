import time
import asyncio
import sys # เพิ่มบรรทัดนี้

# บังคับให้ stdout ใช้ UTF-8 encoding หากยังไม่ได้ใช้ (สำหรับ Python 3.7+)
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# coroutine for a task
async def download_image(name, delay):
    print(f"{time.ctime()} {name} กำลังโหลด...")
    await asyncio.sleep(delay)
    print(f"{time.ctime()} {name} โหลดเสร็จแล้ว!")

# define a main coroutine
async def main():
    # report a message
    print(f"{time.ctime()} main coroutine started")

    # start many tasks
    started_tasks = [asyncio.create_task(download_image(f"image_{i}", i + 1)) for i in reversed(range(3))] 
    # แก้ไข delay ให้เป็น i+1 เพื่อให้มี delay เป็น 1, 2, 3 แทนที่จะเป็น 0, 1, 2

    # allow some of the tasks time to start
    await asyncio.sleep(0.1)

    for task in started_tasks:
        await task

# start the asyncio program
asyncio.run(main())