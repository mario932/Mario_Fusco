def check_empty_array(func):
    def wrapper(arr, *args, **kwargs):
        if not arr:
            print("Array is empty")
            return None
        else:
            return func(arr, *args, **kwargs)
    return wrapper

@check_empty_array
def process_array(arr):
    print("test_arr:", arr)

test_arr = []
process_array(test_arr)




