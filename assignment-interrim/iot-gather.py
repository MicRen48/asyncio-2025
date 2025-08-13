import asyncio, time, random

async def get_temperature():
    await asyncio.sleep(random.uniform(0.5, 2.0))
    return f"{time.ctime()} Temp: 30°C"

async def get_humidity():
    await asyncio.sleep(random.uniform(0.5, 2.0))
    return f"{time.ctime()} Humidity: 60%"

async def get_weather_api():
    await asyncio.sleep(random.uniform(0.5, 2.0))
    return f"{time.ctime()} Weather: Sunny"

async def main():
    start = time.time()

    # รันทั้ง 3 async พร้อมกัน
    temp_task = get_temperature()
    humid_task = get_humidity()
    weather_task = get_weather_api()

    results = await asyncio.gather(temp_task, humid_task, weather_task)

    # แสดงผลลัพธ์ตามลำดับที่ coroutine ถูกส่งเข้าไป
    for r in results:
        print(r)

    print(f"Took {time.time() - start:.2f} seconds")

asyncio.run(main())
