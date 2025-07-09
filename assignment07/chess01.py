import time
from datetime import timedelta

# ---- CONFIG ----
speed = 100  # ความเร็วจำลอง (ยิ่งมาก ยิ่งเร็ว)
Judit_time = 5 / speed     # เวลา Judit ใช้
Opponent_time = 55 / speed # เวลา Opponent ใช้
opponents = 24             # จำนวนกระดาน
move_pairs = 30            # จำนวนคู่เดินหมาก

def game(x):
    # จำลองการเล่นบนกระดานที่ x
    board_start_time = time.perf_counter()
    calculated_board_start_time = 0

    for i in range(move_pairs):
        time.sleep(Judit_time)
        calculated_board_start_time += Judit_time
        print(f"BOARD-{x+1} {i+1} Judit made a move with {int(Judit_time * speed)} secs.")

        time.sleep(Opponent_time)
        calculated_board_start_time += Opponent_time
        print(f"BOARD-{x+1} {i+1} Opponent made move with {int(Opponent_time * speed)} secs.")

    elapsed_real = (time.perf_counter() - board_start_time) * speed
    elapsed_calc = calculated_board_start_time * speed

    print(f"BOARD-{x+1} – >>>>>>>>>>>>>>> Finished move in {elapsed_real:.1f} secs")
    print(f"BOARD-{x+1} – >>>>>>>>>>>>>>> Finished move in {elapsed_calc:.1f} secs (calculated)\n")

    return {
        'board_time': elapsed_real,
        'calculated_board_time': elapsed_calc
    }

# --------- MAIN ---------
if __name__ == "__main__":
    print(f"Number of games: {opponents} games.")
    print(f"Number of move pairs: {move_pairs} pairs.\n")

    start_time = time.perf_counter()
    boards_time = 0
    calculated_board_time = 0

    for board in range(opponents):
        result = game(board)
        boards_time += result['board_time']
        calculated_board_time += result['calculated_board_time']

    # สรุปเวลา
    total_real_time = timedelta(seconds=boards_time)
    total_calc_time = timedelta(seconds=calculated_board_time)

    print("=" * 60)
    print(f"Board exhibition finished for {opponents} opponents in {total_real_time} hr.")
    print(f"Board exhibition finished for {opponents} opponents in {total_calc_time} hr.  (calculated)")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")
    print("=" * 60)
    