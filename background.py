import time

def do_something():
    with open("/tmp/current_time.txt", "w") as f:
        f.write("The time is now " + time.ctime())

def run():
    while True:
        time.sleep(60)
        do_something()

if __name__ == "__main__":
    run()