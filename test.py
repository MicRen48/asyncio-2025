import asyncio
import time
async def download_file(file_name, size_mb, delay_sec):
    start_time = time.time()           
    await asyncio.sleep(delay_sec)   
    end_time = time.time()
    use_time = end_time - start_time   
    speed = size_mb / use_time       
    return {'file_name': file_name,'size_mb': size_mb,'time_sec': use_time,'speed_mbps': speed}
async def main():   
    files = [('File A', 300, 3),('File B', 200, 2),('File C', 100, 1)]    
    tasks = [asyncio.create_task(download_file(name, size, delay)) for name, size, delay in files]   
    results = await asyncio.gather(*tasks)   
    for result in results:
        print(f"{result['file_name']} MB downloaded at {result['speed_mbps']:.2f} MB/s" )            
asyncio.run(main())