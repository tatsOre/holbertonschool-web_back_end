#!/usr/bin/env python3
"""
Module for 0. The basics of async.
0x01. Python - Async
Holberton Web Stack programming Spec ― Back-end
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
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
