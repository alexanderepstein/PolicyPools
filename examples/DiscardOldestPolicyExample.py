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
    iter_times = 20
    # Use with for safe closing of threads
    with DiscardOldestThreadPoolExecutor(max_q_size=5, max_workers=3) as policy_thread_pool:
        iterable = range(iter_times)  # Creating the parameter that will be iterated over
        print("Testing submit")
        future = policy_thread_pool.submit(threaded_func, -1)  # Submit the single future with argument of -1
        # The try catch is only needed if you want to get result from the future
        # Needed in case the future was discarded before it ran
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
Thread -1 finished, Future result: 1, Total Time: 1.0008816719055176

Testing map
Thread 0 started
Thread 1 started
Thread 0 finished
Thread 15 started
Thread 0 Future result: 0, Total Time: 1.0014240741729736
Thread 1 finished
Thread 16 started
Thread 1 Future result: 1, Total Time: 1.0014240741729736
Thread 16 finished
Thread 17 started
Thread 15 finished
Thread 18 started
Thread 15 Future result: 225, Total Time: 1.0008721351623535
Thread 16 Future result: 256, Total Time: 1.0008721351623535
Thread 18 finished
Thread 17 finished
Thread 19 started
Thread 17 Future result: 289, Total Time: 1.000530481338501
Thread 18 Future result: 324, Total Time: 1.000530481338501
Thread 19 finished
Thread 19 Future result: 361, Total Time: 1.0011065006256104
"""