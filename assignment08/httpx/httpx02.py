import httpx

async def fetch(url):
    async with httpx.AsyncClient() as client :
        response = await client.get(url)
        return url, response.status_code

async def main():
    url = [

        "https://example.com"
        "https://httpbin.org/get"
        "https://api.github.com"

    ]
    task = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for url, ststus in results:
        print(f"{url} {ststus}")

asyncio.run(main())