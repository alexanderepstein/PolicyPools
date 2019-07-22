from time import time, sleep

from policypools.BoundedThreadPoolExecutor import BoundedThreadPoolExecutor


def threaded_func(number):
    # do something
    print("Thread %d started" % number)
    start = time()
    sleep(1)
    result = number**2
    time_taken = time()-start
    return number, time_taken, result


if __name__ == '__main__':
    iter_times = 10
    # Use with for safe closing of threads, one more worker than num iterations so that returns work
    with BoundedThreadPoolExecutor(max_q_size=iter_times, num_workers=iter_times+1) as policy_thread_pool:
        iterable = range(iter_times)
        print("Testing submit")
        future = policy_thread_pool.submit(threaded_func, -1)
        thread_number, time_taken, result = future.result()
        print(f"Thread {thread_number} finished, Future result: {result}, Total Time: {time_taken}")
        print("\nTesting map")
        map_object = policy_thread_pool.map(threaded_func, iterable)
        for thread_number, time_taken, result in map_object:
            #  Use the variables in map_object
            print(f"Thread {thread_number} finished, Future result: {result}, Total Time: {time_taken}")

"""
Output:
Testing submit
Thread -1 started
Thread -1 finished, Future result: 1, Total Time: 1.002450704574585

Testing map
Thread 0 started
Thread 1 started
Thread 2 started
Thread 3 started
Thread 4 started
Thread 5 started
Thread 6 started
Thread 7 started
Thread 8 started
Thread 9 started
Thread 0 finished, Future result: 0, Total Time: 1.0035955905914307
Thread 1 finished, Future result: 1, Total Time: 1.001927137374878
Thread 2 finished, Future result: 4, Total Time: 1.00215744972229
Thread 3 finished, Future result: 9, Total Time: 1.0011637210845947
Thread 4 finished, Future result: 16, Total Time: 1.0038244724273682
Thread 5 finished, Future result: 25, Total Time: 1.0028643608093262
Thread 6 finished, Future result: 36, Total Time: 1.0027830600738525
Thread 7 finished, Future result: 49, Total Time: 1.0017783641815186
Thread 8 finished, Future result: 64, Total Time: 1.0007481575012207
Thread 9 finished, Future result: 81, Total Time: 1.0044500827789307
"""