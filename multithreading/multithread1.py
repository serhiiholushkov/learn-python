import threading
import time


def walk_dog():
    time.sleep(8)  # sleep for 8 seconds to simulate a long task
    print("Walking the dog")


def take_out_trash():
    time.sleep(3)  # sleep for 3 seconds to simulate a shorter task
    print("Taking out the trash")


def get_mail():
    time.sleep(5)  # sleep for 5 seconds to simulate a medium task
    print("Getting the mail")


# walk_dog()
# take_out_trash()
# get_mail()
# print("All tasks completed sequentially")

# Now with threading
thread1 = threading.Thread(target=walk_dog)
thread2 = threading.Thread(target=take_out_trash)
thread3 = threading.Thread(target=get_mail)
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
# without join, the main thread may exit before the threads complete
print("All tasks started in parallel")
