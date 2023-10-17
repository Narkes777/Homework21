import random
import time
import multiprocessing
import psutil

def random_number(filename):
    random_num = random.randint(1, 1000)
    time.sleep(1)
    with open(filename, 'w') as file:
        file.write(str(random_num))
        
start_time = time.time()

for i in range(1000):
    filename = f'file_{i}.txt'
    random_number(filename)

end_time = time.time()
execution_time = end_time - start_time

print(f'Total time: {execution_time} seconds')

def random_number_file(filename):
    random_num = random.randint(1, 1000)
    time.sleep(1)
    with open(filename, 'w') as file:
        file.write(str(random_num))
    
    cpu_load = psutil.cpu_percent(interval=0.1)
    print(f'CPU load{filename}: {cpu_load}%')

if __name__ == "__main__":
    start_time = time.time()

    with multiprocessing.Pool() as pool:
        filenames = [f'file_{i}.txt' for i in range(1000)]
        pool.map(random_number_file, filenames)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f'Total time taken for concurrent execution: {execution_time} seconds')