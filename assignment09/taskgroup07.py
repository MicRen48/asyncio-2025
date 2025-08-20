import asyncio

async def work(n, fail=False):
    await asyncio.sleep(n)  # Simulate work
    if fail:
        raise ValueError(f"Task {n} failed")
    return f"Task {n} OK"

async def main():
    results = await asyncio.gather(
        work(1, fail=True),
        work(2),
        work(3)
        return_exceptions=True  # Collect exceptions instead of raising
    )
    print("Results:",results)

asyncio.run(main())