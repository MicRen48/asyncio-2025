import httpx, asyncio
import folium

REGISTRY_URL = "http://127.0.0.1:9000"

async def fetch_aggregate():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{REGISTRY_URL}/aggregate")
        return r.json()["weather_data"]

async def main():
    data = await fetch_aggregate()

    # สร้างแผนที่
    m = folium.Map(location=[18.7883, 98.9853], zoom_start=10)

    for d in data:
        folium.Marker(
            [18.7883, 98.9853],
            popup=f"{d['student_id']}\n{d['province']}\n{d['temperature']}°C, {d['description']}"
        ).add_to(m)

    m.save("weather_map.html")
    print("Map saved as weather_map.html")

if __name__ == "__main__":
    asyncio.run(main())
