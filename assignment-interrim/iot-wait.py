import asyncio, time, random

async def get_temperature():
    await asyncio.sleep(random.uniform(0.5, 2.0))
    return "Temp: 30°C"

async def get_humidity():
    await asyncio.sleep(random.uniform(0.5, 2.0))
    return "Humidity: 60%"

async def get_weather_api():
    await asyncio.sleep(random.uniform(0.5, 2.0))
    return "Weather: Sunny"

async def main():
    # Use time to measure the total execution time
    start_time = time.time()

    # Create a set of tasks from the coroutines
    tasks = {
        asyncio.create_task(get_temperature()),
        asyncio.create_task(get_humidity()),
        asyncio.create_task(get_weather_api()),
    }

    # Continuously wait for the first task to complete and print its result
    # until all tasks are done.
    while tasks:
        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            result = task.result()
            print(f"{time.ctime()} -> {result}")

    end_time = time.time()
    print(f"\nTook {end_time - start_time:.2f} seconds")

asyncio.run(main())