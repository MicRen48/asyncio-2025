import asyncio
import random 

async def read_temperature():
    await asyncio.sleep(1)  # Simulate sensor delay
    return f"Temperature{random.uniform(20.0, 30.0)}°c"
  # Simulate temperature reading

async def read_humidity():
    await asyncio.sleep(1)  # Simulate sensor delay
    return f"Humidity{random.uniform(40.0, 70.0)}%"

async def read_pressure():
    await asyncio.sleep(1)  # Simulate sensor delay
    return f"Pressure{random.uniform(900.0, 1100.0)}hPa"

async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(read_temperature())
        t2 = tg.create_task(read_humidity())
        t3 = tg.create_task(read_pressure())

    print(await t1)
    print(await t2)
    print(await t3)

asyncio.run(main())


    