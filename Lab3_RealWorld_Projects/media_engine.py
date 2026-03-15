def monitor(func):
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper

def play_count_stream(limit):
    for i in range(limit):
        if i % 2 == 0:  # even numbers only
            yield i ** 2

@monitor
def run_stream(limit):
    counts = list(play_count_stream(limit))
    print("Generated Play Counts:", counts)
    print("Total Plays:", sum(counts))
    print("Number of Records Processed:", len(counts))