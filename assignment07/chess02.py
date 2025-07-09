import asyncio
from datetime import timedelta

# ---- CONFIG ----
speed = 100
Judit_time = 5 / speed
Opponent_time = 55 / speed
opponents = 24
move_pairs = 30

async def game(x):
    # ใช้ asyncio จำลองเวลาจริงแบบ async
    board_start_time = asyncio.get_event_loop().time()
    calculated_board_time = 0

    for i in range(move_pairs):
        await asyncio.sleep(Judit_time)
        calculated_board_time += Judit_time
        print(f"BOARD-{x+1} {i+1} Judit made a move with {int(Judit_time * speed)} secs.")

        await asyncio.sleep(Opponent_time)
        calculated_board_time += Opponent_time
        print(f"BOARD-{x+1} {i+1} Opponent made move with {int(Opponent_time * speed)} secs.")

    elapsed_real = (asyncio.get_event_loop().time() - board_start_time) * speed
    elapsed_calc = calculated_board_time * speed

    print(f"BOARD-{x+1} >>>>>>>>>> Finished move in {elapsed_real:.1f} secs")
    print(f"BOARD-{x+1} >>>>>>>>>> Finished move in {elapsed_calc:.1f} secs (calculated)\n")

    return {
        'board_time': elapsed_real,
        'calculated_board_time': elapsed_calc
    }

async def main():
    print(f"Number of games: {opponents} games.")
    print(f"Number of move pairs: {move_pairs} pairs.\n")

    start_time = asyncio.get_event_loop().time()

    # สร้าง task ทุกกระดานให้ทำงานพร้อมกัน
    tasks = [game(i) for i in range(opponents)]
    results = await asyncio.gather(*tasks)

    boards_time = sum(result['board_time'] for result in results)
    calculated_time = sum(result['calculated_board_time'] for result in results)

    print("=" * 60)
    print(f"Board exhibition finished for {opponents} opponents in {timedelta(seconds=boards_time)} hr.")
    print(f"Board exhibition finished for {opponents} opponents in {timedelta(seconds=calculated_time)} hr. (calculated)")
    print(f"Finished in {round(asyncio.get_event_loop().time() - start_time)} secs.")
    print("=" * 60)

# Run async main
asyncio.run(main())
