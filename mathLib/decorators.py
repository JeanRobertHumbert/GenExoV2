import time

def time_logger(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Tiem perf : {end-start}s")
        return result
    return wrapper

@time_logger
def process_input(n):
    return(n**2)


if __name__=="__main__":
    print(process_input(5))
