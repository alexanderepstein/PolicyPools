from threading import Thread
from os import cpu_count

from policypools.AbstractThreadPool import AbstractThreadPool


class InfiniteThreadPool(AbstractThreadPool):

    def __init__(self):
        """
        Infinite thread pool, very large queue size and num workers set based off computer specs
        """
        super(InfiniteThreadPool, self).__init__(9999999999, min(32, cpu_count() + 4))

    def submit(self, thread: Thread):
        """
        Submits a new thread
        :param thread: the given thread to run
        :return: None
        """
        self._thread_q.put(thread)