from time import time, sleep

from policypools.DiscardOldestThreadPoolExecutor import DiscardOldestThreadPoolExecutor


def threaded_func(number):
    # do something
    print("Thread %d started" % number)
    start = time()
    sleep(1)
    result = number**2
    time_taken = time()-start
    print("Thread %d finished" % number)
    return number, time_taken, result


if __name__ == '__main__':
    iter_times = 100000
    # Use with for safe closing of threads
    with DiscardOldestThreadPoolExecutor(max_q_size=5, max_workers=3) as policy_thread_pool:
        iterable = range(iter_times)  # Creating the parameter that will be iterated over
        print("Testing submit")
        future = policy_thread_pool.submit(threaded_func, -1)  # Submit the single future with argument of -1
        # The try catch is only needed if you want to get result from the future
        # Needed in case the future was discarded before it ran
        try:
            thread_number, time_taken, result = future.result()  # Get the result of that future
        except ValueError as ex:
            print(ex)
            pass
        if result is not None:
            # A submitted thread may return None
            print(f"Thread {thread_number} finished, Future result: {result}, Total Time: {time_taken}")
        print("\nTesting map")
        map_object = policy_thread_pool.map(threaded_func, iterable)  # Mapping the function over each value in iterable
        for thread_number, time_taken, result in map_object:
            #  Use the variables in map_object
            print(f"Thread {thread_number} Future result: {result}, Total Time: {time_taken}")
"""
Output:
Testing submit
Thread -1 started
Thread -1 finished
Thread -1 finished, Future result: 1, Total Time: 1.0051846504211426

Testing map
Thread 0 started
Thread 1 started
Thread 0 finished
Thread 1 finished
Thread 60631 started
Thread 60634 started
Thread 0 Future result: 0, Total Time: 1.00758957862854
Thread 1 Future result: 1, Total Time: 1.0077106952667236
Thread 60631 finished
Thread 99995 started
Thread 60634 finished
Thread 99996 started
Thread 60631 Future result: 3676118161, Total Time: 1.0035748481750488
Thread 60634 Future result: 3676481956, Total Time: 1.00374436378479
Thread 99996 finished
Thread 99997 started
Thread 99995 finished
Thread 99998 started
Thread 99995 Future result: 9999000025, Total Time: 1.0059700012207031
Thread 99996 Future result: 9999200016, Total Time: 1.0056214332580566
Thread 99998 finished
Thread 99999 started
Thread 99997 finished
Thread 99997 Future result: 9999400009, Total Time: 1.0017688274383545
Thread 99998 Future result: 9999600004, Total Time: 1.0013201236724854
Thread 99999 finished
Thread 99999 Future result: 9999800001, Total Time: 1.0040488243103027
"""