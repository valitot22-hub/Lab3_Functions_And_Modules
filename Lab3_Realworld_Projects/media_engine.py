import functools

def monitor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper

def signal_shutdown(power, count=0):
    if power <= 0:
        print("Base case reached: power is 0")
        return count
    
    print(f"Current signal strength: {power}")
    return signal_shutdown(power - 1, count + 1)

def play_count_stream(limit):
    for i in range(0, limit + 1):
        if i % 2 == 0:
            yield i ** 2