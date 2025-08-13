# Question
1. ถ้าสร้าง asyncio.create_task(*tasks) ที่ไม่มี await ที่ main() เกิดอะไรบ้าง
   1. Task จะเริ่มทำงานทันทีแบบ background แต่ main() ไม่รอให้meเสร็จ อาจทำให้โปรแกรมจบก่อน task เสร็จ
   2. งานที่ยังไม่เสร็จจะถูก ยกเลิกทันที เมื่อ event loop ปิด ทำให้ผลลัพธ์หาย หรือไม่เกิดการทำงานเต็มที่
   3. ไม่สามารถจัดการข้อผิดพลาด (exception) ได้ง่าย เพราะไม่มีจุด await มาดึง result() หรือ exception()
2. ความแตกต่างระหว่าง asyncio.gather(*tasks) กับ asyncio.wait(tasks) คืออะไร
   1. gather() จะคืนค่าผลลัพธ์ของทุก task ตามลำดับที่ส่งเข้าไป แต่ wait() จะคืนค่าเป็น (done, pending) ซึ่งเป็น set ของ task objects
   2. gather() ค่าdefault จะยกexceptionของ task แรกที่ error แต่ wait() จะไม่ยก exception อัตโนมัติต้องไปตรวจเองจาก done
   3. gather() รอให้ task ทั้งหมดเสร็จ (default) แต่ wait() จะเลือกเงื่อนไขการรอได้(FIRST_COMPLETED, FIRST_EXCEPTION, ALL_COMPLETED)
3. สร้าง create_task() และ coroutine ของ http ให้อะไรต่างกัน
   1. create_task() ใช้เมื่ออยากเริ่มรัน coroutine ทันทีแล้วไปทำงานอื่นต่อพร้อมเก็บตัว task ไว้เพื่อ await หรือผูก callback ทีหลัง
   2. เรียก coroutine ตรง ๆ (เช่น await fetch()) จะรอให้ coroutine นั้นเสร็จก่อนแล้วค่อยทำต่อไม่สามารถทำงานอื่นระหว่างรอได้(ถ้าไม่ใช้ concurrent tools อื่น)
   3. ข้อดีของ create_task() คือสามารถเริ่มงานหลายๆอย่างพร้อมกันและจัดการมันในภายหลังได้ เช่น ทำ HTTP request หลายอันพร้อมกันโดยไม่ต้องรอทีละอัน
