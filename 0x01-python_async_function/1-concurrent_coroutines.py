#!/usr/bin/env python3
"""
Module for 1. Let's execute multiple coroutines at the same time with async.
0x01. Python - Async
Holberton Web Stack programming Spec ― Back-end
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Method that executes multiples coroutines at the same time

    Parameters
    ----------
        n : int
        max_delay : int
    Returns
    -------
        List
            list of the delays in ascending order
    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    # h = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return [await task for task in asyncio.as_completed(tasks)]
