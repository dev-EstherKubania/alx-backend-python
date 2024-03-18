#!/usr/bin/env python3
"""
Module to demonstrate basic asynchronous syntax in Python
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    seconds and eventually returns it.

    Args:
        max_delay (int): The maximum delay to wait for (default is 10).

    Returns:
        float: The random delay waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
