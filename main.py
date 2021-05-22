import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        first_time = time.time()
        function()
        second_time = time.time()
        diff = second_time - first_time
        print(f"The running time for {function.__name__} is {diff}s") 
    return wrapper_function
    
    
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator        
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()