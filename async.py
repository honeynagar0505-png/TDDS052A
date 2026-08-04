import asyncio
import time

async def verify_student():
    print("Verifying Student.....")
    await asyncio.sleep(2)
    print("Student Verified\n")
    
async def fetch_attendance():
    print("Fetching Attendance....")
    await asyncio.sleep(3)
    print("Attendance Loaded\n")
    
async def fetch_marks():
    print("Fetching Marks...")
    await asyncio.sleep(2)
    print("Marks Loaded\n") 

async def main():
    
    start = time.time()
    
    await verify_student()
    
    attendance_task = asyncio.create_task(fetch_attendance())
    marks_task = asyncio.create_task(fetch_marks())
    
    await attendance_task
    await marks_task

    end = time.time()
    print(f"Total Time Taken: {end - start:.2f} seconds")   
    
asyncio.run(main())

import asyncio
import time

async def verify_student():
    print("Verifying Student.....")
    await asyncio.sleep(2)
    print("Student Verified\n")
    
async def fetch_attendance():
    print("Fetching Attendance....")
    await asyncio.sleep(3)
    print("Attendance Loaded\n")
    
async def fetch_marks():
    print("Fetching Marks...")
    await asyncio.sleep(2)
    print("Marks Loaded\n") 

async def main():
    
    start = time.time()
    
    await verify_student()
    
    attendance_task = asyncio.create_task(fetch_attendance())
    marks_task = asyncio.create_task(fetch_marks())
    
    await attendance_task
    await marks_task

    end = time.time()
    print(f"Total Time Taken: {end - start:.2f} seconds")   
    
asyncio.run(main())
