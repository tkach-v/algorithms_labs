import time


def get_exec_time(f):
    def wrapper(*args):
        start = time.time()
        result = f(*args)
        end = time.time()
        exec_time = (end - start)
        return exec_time, result

    return wrapper


@get_exec_time
def selection_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        max_elem_idx = 0
        for j in range(1, i + 1):
            if arr[j] > arr[max_elem_idx]:
                max_elem_idx = j
        arr[i], arr[max_elem_idx] = arr[max_elem_idx], arr[i]
    return arr
