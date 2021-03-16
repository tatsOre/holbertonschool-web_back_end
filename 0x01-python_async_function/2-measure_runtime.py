#!/usr/bin/env python3
"""
Module for 2. Measure the runtime.
0x01. Python - Async
Holberton Web Stack programming Spec ― Back-end
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Method that measures the total execution time for `wait_n(n, max_delay)`

    Parameters
    ----------
        n : int
        max_delay : int
    Returns
    -------
        float
            average elapsed runtime
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
