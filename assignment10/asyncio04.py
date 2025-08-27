import asyncio
from datetime import datetime

def time() -> str:
    return datetime.now().strftime("%a %b %d %H:%M:%S %Y")

# Producer: ลูกค้าใส่ออเดอร์ลงคิว
async def customer(name: str, items: list[str], q: asyncio.Queue):
    print(f"[{time()}] ({name}) finished shopping: {items}")
    await q.put((name, items))

# Consumer: แคชเชียร์ดึงออเดอร์จากหลายคิว
async def cashier(cid: str, per_item_sec: float, queues: list[asyncio.Queue]):
    try:
        while True:
            # สร้าง task สำหรับทุกคิว
            tasks = []
            for q in queues:
                t = asyncio.create_task(q.get())
                t.queue = q  # ผูก queue ไว้กับ task
                tasks.append(t)

            done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

            # เก็บงานที่เสร็จแล้ว
            for t in done:
                name, items = t.result()
                print(f"[{time()}] [{cid}] processing {name} with orders {items}")
                for _ in items:
                    await asyncio.sleep(per_item_sec)
                print(f"[{time()}] [{cid}] finished {name}")
                t.queue.task_done()   # ใช้คิวที่ผูกมากับ task

            # ยกเลิกงานที่ยัง pending
            for t in pending:
                t.cancel()

    except asyncio.CancelledError:
        print(f"[{time()}] [{cid}] closed")
        raise

async def main():
    q = [asyncio.Queue() for _ in range(5)]  # 5 คิว

    # แคชเชียร์ 2 คน ใช้คิวทั้งหมด
    cashiers = {
        "Cashier-1": (1, q),
        "Cashier-2": (2, q),
    }

    cashier_tasks = [
        asyncio.create_task(cashier(cid, speed, queues))
        for cid, (speed, queues) in cashiers.items()
    ]

    customers = [
        ("Alice",   ["Apple", "Banana", "Milk"]),
        ("Bob",     ["Bread", "Cheese"]),
        ("Charlie", ["Eggs", "Juice", "Butter"]),
        ("Diana",   ["Yogurt"]),
        ("Eve",     ["Cereal", "Coffee"]),
        ("Frank",   ["Tea", "Sugar", "Flour", "Rice"]),
        ("Grace",   ["Chicken", "Beef"]),
        ("Hank",    ["Fish", "Lettuce", "Tomato"]),
        ("Ivy",     ["Pasta", "Sauce"]),
        ("Jack",    ["Snacks", "Soda", "Ice Cream"]),
    ]

    
    jobs = [
        asyncio.create_task(customer(name, items, q[i % len(q)]))
        for i, (name, items) in enumerate(customers)
    ]
    await asyncio.gather(*jobs)

    # รอให้ทุกคิวเสร็จ
    await asyncio.gather(*(queue.join() for queue in q))

    # ปิดเคาน์เตอร์
    for t in cashier_tasks:
        t.cancel()
    await asyncio.gather(*cashier_tasks, return_exceptions=True)

    print(f"[{time()}] [Main] Supermarket closed!")

if __name__ == "__main__":
    asyncio.run(main())
