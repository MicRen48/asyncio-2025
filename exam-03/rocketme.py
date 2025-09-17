import time
import aiohttp
import asyncio

student_id = "1234567890"


async def fire_rocket(name: str, t0: float):
    url = f"http://172.16.2.117:8088/fire/{student_id}"
    start_time = time.perf_counter() - t0  # เวลาเริ่มสัมพัทธ์
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            time_to_target = data['time_to_target']
            end_time = start_time + time_to_target
            return {
                "name": name,
                "start_time": start_time,
                "time_to_target": time_to_target,
                "end_time": end_time
            }

async def main():
    t0 = time.perf_counter()  # เวลาเริ่มของชุด rockets

    print("Rocket prepare to launch ...")  # แสดงตอนเริ่ม main

    # สร้าง task ยิง rocket 3 ลูกพร้อมกัน
    tasks = [asyncio.create_task(fire_rocket(f"Rocket-{i+1}", t0)) for i in range(3)]

    # รอให้ทุก task เสร็จและเก็บผลลัพธ์
    results = await asyncio.gather(*tasks)

    # เรียงลำดับ rocket ตามเวลาที่ถึงจุดหมาย
    results = sorted(results, key=lambda r: r['end_time'])

    print("Rockets fired:")
    for r in results:
        print(f"{r['name']} | start_time: {r['start_time']:.2f} sec | time_to_target: {r['time_to_target']:.2f} sec | end_time: {r['end_time']:.2f} sec")

    # แสดงเวลารวมทั้งหมดตั้งแต่ยิงลูกแรกจนลูกสุดท้ายถึงจุดหมาย
    t_total = max(r['end_time'] for r in results)
    print(f"\nTotal time for all rockets: {t_total:.2f} sec")

