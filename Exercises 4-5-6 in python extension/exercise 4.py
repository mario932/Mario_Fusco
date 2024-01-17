import time

def time_a_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f" {execution_time} seconds to execute.")
        return result
    return wrapper

@time_a_function
def mysleep():
    time.sleep(5)
    print('executed')

mysleep()