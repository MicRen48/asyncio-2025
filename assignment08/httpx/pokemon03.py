import asyncio
import httpx

async def fetch_pokemon_name():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        
        print("Name:", data["name"])
        print("ID:", data["id"])
        print("Height:", data["height"])
        print("Weight:", data["weight"])
        print("Types:", [t["type"]["name"] for t in data["types"]])


asyncio.run(fetch_pokemon_name())
