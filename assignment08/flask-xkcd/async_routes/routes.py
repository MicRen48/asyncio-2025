import time
import random
import asyncio
import httpx
from flask import Blueprint, render_template, current_app

# Create a Blueprint for async routes
async_bp = Blueprint("async", __name__)

# Async helper function to fetch a single XKCD JSON by URL
async def get_xkcd(client, url):
    response = await client.get(url)
    print(f"{time.ctime()} - get {url}")
    return response.json()

# Async helper function to fetch multiple XKCD comics
async def get_xkcds():
    NUMBER_OF_XKCD = current_app.config["NUMBER_OF_XKCD"]
    rand_list = [random.randint(0, 300) for _ in range(NUMBER_OF_XKCD)]

    async with httpx.AsyncClient() as client:
        tasks = []
        for number in rand_list:
            url = f'https://xkcd.com/{number}/info.0.json'
            tasks.append(get_xkcd(client, url))

        xkcd_data = await asyncio.gather(*tasks)
    return xkcd_data

# Async route: GET /async/
@async_bp.route('/')
async def home():
    start_time = time.perf_counter()
    xkcds = await get_xkcds()
    end_time = time.perf_counter()

    print(f"{time.ctime()} - Get {len(xkcds)} xkcd. Time taken: {end_time - start_time} seconds")

    return render_template(
        'async.html',
        title="XKCD Async Flask (httpx)",
        heading="XKCD Async Version (httpx)",
        xkcds=xkcds,
        end_time=end_time,
        start_time=start_time
    )
