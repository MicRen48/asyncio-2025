import asyncio
import httpx
import time

async def fetch_ability_list(client):
    url = "https://pokeapi.co/api/v2/ability/?limit=20"
    response = await client.get(url)
    data = response.json()

    return data["results"]

async def fetch_ability_detail(client, ability_url):
    response = await client.get(ability_url)
    data = response.json()
    # data['pokemon'] คือ list ของ dict ที่มี 'pokemon' กับ 'is_hidden' 
    pokemon_list = data.get('pokemon', [])
    count = len(pokemon_list)
    ability_name = data.get('name', 'unknown').title()
    return ability_name, count

async def main():
    start = time.time()
    async with httpx.AsyncClient() as client:
        ability_list = await fetch_ability_list(client)

        tasks = [
            fetch_ability_detail(client, ability['url'])
            for ability in ability_list
        ]

        results = await asyncio.gather(*tasks)

        for name, count in results:
            print(f"Ability: {name:<15} -> Pokemon count: {count}")
            
    end = time.time()
    
asyncio.run(main())

