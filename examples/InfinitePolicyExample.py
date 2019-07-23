from time import time, sleep

from policypools.InfiniteThreadPoolExecutor import InfiniteThreadPoolExecutor


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
    iter_times = 1000
    # Use with for safe closing of threads
    with InfiniteThreadPoolExecutor() as policy_thread_pool:  # No need to pass parameters to this policy
        iterable = range(iter_times)  # Creating the parameter that will be iterated over
        print("Testing submit")
        future = policy_thread_pool.submit(threaded_func, -1)  # Submit the single future with argument of -1
        thread_number, time_taken, result = future.result()  # Get the result of that future
        print(f"Thread {thread_number} finished, Future result: {result}, Total Time: {time_taken}")
        print("\nTesting map")
        map_object = policy_thread_pool.map(threaded_func, iterable)  # Mapping the function over each value in iterable
        for thread_number, time_taken, result in map_object:
            #  Use the variables in map_object
            print(f"Thread {thread_number} Future result: {result}, Total Time: {time_taken}")

"""
Output:
Run on your own, this one is big 
"""