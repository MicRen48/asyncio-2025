import asyncio
import httpx
import time

pokemon_names = [
    "pikachu", "bulbasaur", "charmander", "squirtle", "eevee",
    "snorlax", "gengar", "mewtwo", "psyduck", "jigglypuff"
]

results = []

async def fetch_pokemon_data(name, client):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = await client.get(url)
    data = response.json()

    results.append({
        "name": data["name"].title(),
        "id": data["id"],
        "base_xp": data["base_experience"]
    })

def get_base_xp(pokemon):
    return pokemon["base_xp"]

async def main():
    start = time.time()
    async with httpx.AsyncClient() as client:
        tasks = [fetch_pokemon_data(name, client) for name in pokemon_names]
        await asyncio.gather(*tasks)
    end = time.time()

    clean_results = [res for res in results if res is not None]
    sorted_pokemon = sorted(clean_results, key=get_base_xp, reverse=True)

    
    for p in sorted_pokemon:
        print(f"{p['name']:<12} -> ID: {p['id']:<4} Base Xp: {p['base_xp']:<8}")

    
asyncio.run(main())
