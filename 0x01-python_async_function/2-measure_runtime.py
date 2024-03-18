#!/usr/bin/env python3
"""
Module to demonstrate concurrent coroutines in Python
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with the specified
    max_delay and returns the list of all the delays.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random.

    Returns:
        List[float]: The list of all the delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)
