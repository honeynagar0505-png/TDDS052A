<<<<<<< HEAD
import time

def verify_student():
    print("Verifying Student.....")
    time.sleep(2)
    print("Student Verified\n")
    
def fetch_attendance():
    print("Fetching Attendance....")
    time.sleep(3)
    print("Attendance Loaded\n")
    
def fetch_marks():
    print("Fetching Marks...")
    time.sleep(2)
    print("Marks Loaded\n")
    
print("========== Student Portal ==========\n")

start = time.time()

verify_student()
fetch_attendance()
fetch_marks()

end = time.time()

=======
import time

def verify_student():
    print("Verifying Student.....")
    time.sleep(2)
    print("Student Verified\n")
    
def fetch_attendance():
    print("Fetching Attendance....")
    time.sleep(3)
    print("Attendance Loaded\n")
    
def fetch_marks():
    print("Fetching Marks...")
    time.sleep(2)
    print("Marks Loaded\n")
    
print("========== Student Portal ==========\n")

start = time.time()

verify_student()
fetch_attendance()
fetch_marks()

end = time.time()

>>>>>>> 0308120439f88290db45a18060df05bc716035da
print(f"\nTotal Time ={end-start:.2f} seconds")