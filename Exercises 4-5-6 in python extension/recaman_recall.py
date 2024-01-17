import time
import recaman_module as rc


def time_generate_recaman_sequence(n):
    start_time = time.time()
    result = rc.generate_recaman_sequence(n)
    end_time = time.time()
    return result, end_time - start_time

if __name__ == "__main__":
    n = int(input('Insert the number of elements in the sequence: '))
    
    result, execution_time = time_generate_recaman_sequence(n)
    
    print(f"Recaman sequence: {result}")
    print(f"Execution time: {execution_time} seconds")