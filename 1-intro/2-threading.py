import sys
sys.stdout.reconfigure(encoding='utf-8')

import time
import threading
from datetime import datetime

def make_burger(student_id):
    start_time = time.time()  
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] เริ่มทำเบอร์เกอร์ให้นักเรียนคนที่ {student_id}")
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 1. ทอดเบอร์เกอร์...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 2. ทอดไก่...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 3. ใส่ผักและชีส...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 4. ห่อเบอร์เกอร์...")
    time.sleep(5)

    end_time = time.time()
    elapsed = end_time - start_time
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] เสร็จแล้ว! เบอร์เกอร์ของนักเรียนคนที่ {student_id} ใช้เวลา {elapsed:.2f} วินาที")

def main():
    start = time.time()
    
    threads = []
    for i in range(1, 6):
        t = threading.Thread(target=make_burger, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    end = time.time()
    total_elapsed = end - start
    print(f"[{datetime.now().strftime('%H:%M:%S')}] รวมเวลาทั้งหมด: {total_elapsed:.2f} วินาที")

if __name__ == "__main__":
    main()
