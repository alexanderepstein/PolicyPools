from time import time, sleep

from policypools.DiscardNewestThreadPoolExecutor import DiscardNewestThreadPoolExecutor


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
    iter_times = 20
    # Use with for safe closing of threads
    with DiscardNewestThreadPoolExecutor(max_q_size=5, max_workers=3) as policy_thread_pool:
        iterable = range(iter_times)  # Creating the parameter that will be iterated over
        print("Testing submit")
        future = policy_thread_pool.submit(threaded_func, -1)  # Submit the single future with argument of -1
        try:
            thread_number, time_taken, result = future.result()  # Get the result of that future
            print(f"Thread {thread_number} finished, Future result: {result}, Total Time: {time_taken}")
        except ValueError as ex:
            print(ex)
            pass
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
Thread -1 finished, Future result: 1, Total Time: 1.0007412433624268

Testing map
Thread 0 started
Thread 1 started
Thread 0 finished
Thread 2 started
Thread 0 Future result: 0, Total Time: 1.0007507801055908
Thread 1 finished
Thread 3 started
Thread 1 Future result: 1, Total Time: 1.001140832901001
Thread 2 finished
Thread 4 started
Thread 2 Future result: 4, Total Time: 1.000213384628296
Thread 3 finished
Thread 5 started
Thread 3 Future result: 9, Total Time: 1.0004138946533203
Thread 4 finished
Thread 19 started
Thread 4 Future result: 16, Total Time: 1.0008084774017334
Thread 5 finished
Thread 5 Future result: 25, Total Time: 1.0005035400390625
Thread 19 finished
Thread 19 Future result: 361, Total Time: 1.001143455505371
"""