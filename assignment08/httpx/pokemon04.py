import asyncio
import httpx
import time

pokemon_names = [
    "pikachu", "bulbasaur", "charmander", "squirtle", "eevee",
    "snorlax", "gengar", "mewtwo", "psyduck", "jigglypuff"
]

async def fetch_pokemon_data(name, client):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = await client.get(url)
    data = response.json()

    print(f"{data['name'].title()} -> ID: {data['id']}, Type(s): {[t['type']['name'] for t in data['types']]}")
async def main():
    start = time.time()
    async with httpx.AsyncClient() as client:
        tasks = [fetch_pokemon_data(name, client) for name in pokemon_names]
        await asyncio.gather(*tasks)
    end = time.time()
    print("Total time:", round(end - start, 2), "seconds")

asyncio.run(main())
