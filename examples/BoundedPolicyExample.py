from time import time, sleep

from policypools.BoundedThreadPoolExecutor import BoundedThreadPoolExecutor


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
    iter_times = 10
    # Use with for safe closing of threads
    # the condition max_q_size + max_workers - 1 = iter_times
    # must be met for all threads to run successfully otherwise queue.Full will be thrown
    with BoundedThreadPoolExecutor(max_q_size=5, max_workers=6) as policy_thread_pool:
        iterable = range(iter_times)  # Creating the parameter that will be iterated over
        print("Testing submit")
        future = policy_thread_pool.submit(threaded_func, -1)  # Submit the single future with argument of -1
        thread_number, time_taken, result = future.result()  # Get the result of that future
        print(f"Thread {thread_number} finished, Future result: {result}, Total Time: {time_taken}")
        print("\nTesting map")
        map_object = policy_thread_pool.map(threaded_func, iterable)  # Mapping the function over each value in iterable
        for thread_number, time_taken, result in map_object:
            #  Use the variables in map_object
            print(f"Thread Future result: {result}, Total Time: {time_taken}")

"""
Output:
Testing submit
Thread -1 started
Thread -1 finished
Thread -1 finished, Future result: 1, Total Time: 1.005838394165039

Testing map
Thread 0 started
Thread 1 started
Thread 2 started
Thread 3 started
Thread 4 started
Thread 0 finished
Thread 5 started
Thread Future result: 0, Total Time: 1.0003840923309326
Thread 3 finished
Thread 2 finished
Thread 4 finished
Thread 6 started
Thread 1 finished
Thread 7 started
Thread 8 started
Thread Future result: 1, Total Time: 1.0060534477233887
Thread 9 started
Thread Future result: 4, Total Time: 1.0047509670257568
Thread Future result: 9, Total Time: 1.0047509670257568
Thread Future result: 16, Total Time: 1.0049095153808594
Thread 5 finished
Thread Future result: 25, Total Time: 1.0016987323760986
Thread 7 finished
Thread 9 finished
Thread 6 finished
Thread Future result: 36, Total Time: 1.0022680759429932
Thread Future result: 49, Total Time: 1.0020081996917725
Thread 8 finished
Thread Future result: 64, Total Time: 1.001269817352295
Thread Future result: 81, Total Time: 1.0010099411010742
"""