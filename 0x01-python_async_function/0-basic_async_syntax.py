#!/usr/bin/env python3
"""
Module for 0. The basics of async.
0x01. Python - Async
Holberton Web Stack programming Spec ― Back-end
    ->
    random.random() -> Random float:  0.0 <= x < 1.0
    random.uniform(a, b) -> Random float:  a <= x < b
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Parameters
    ----------
        max_delay : int
    Returns
    -------
        float
            Random delay between 0 and `max_delay`
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
