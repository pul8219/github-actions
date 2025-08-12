import os
import time
import threading

current_path = os.path.dirname(os.path.abspath(__file__))
all_items = os.listdir(current_path)
files = [item for item in all_items if os.path.isfile(os.path.join(current_path, item))]
files.remove('test.py')

keyword = "Traceback"

def check_log_file(filename):
    try:
        time.sleep(1)
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        if keyword in content:
            print(f"[MATCH] '{keyword}' string is detected in file {filename}.")
        else:
            print(f"[NO MATCH] '{keyword}' string is not detected in file {filename}.")
    
    except FileNotFoundError:
        print(f"[ERROR] {filename} file not found.")
    except Exception as e:
        print(f"[ERROR] {filename} unexpected error occured. - {e}")

threads = []
start_time = time.time()
for f in files:
    t = threading.Thread(target=check_log_file, args=(f,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Execution time: {time.time() - start_time:.2f}s")
print("Successfully script executed")

