# --- Inputs ---
SEED_NUM = 3
FAVORITE_ARTIST = "CUP OF JOE"
CONTROL_NUM = max(1, SEED_NUM)

# --- Secure Access System ---
from access_control import compute_access_level, validate_access, audit_log

@audit_log
def run_authorization():
    level = compute_access_level(CONTROL_NUM, FAVORITE_ARTIST)
    decision = validate_access(level, CONTROL_NUM)
    print("Access Level:", level)
    print("Threshold:", CONTROL_NUM * 5)
    print("Final Decision:", decision)

run_authorization()

# --- Recursive Signal Shutdown ---
def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

@audit_log
def signal_shutdown(power):
    if power == 0:
        return 0
    print("Signal Strength:", power)
    return 1 + signal_shutdown(power - 1)

power = CONTROL_NUM + len(FAVORITE_ARTIST)
total_calls = signal_shutdown(power)
print("Total Recursive Calls:", total_calls)

# --- Streaming Media Analytics ---
from media_engine import run_stream

limit = CONTROL_NUM + len(FAVORITE_ARTIST)
run_stream(limit)