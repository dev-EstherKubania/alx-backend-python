import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that takes an integer max_delay and returns an asyncio.Task.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: An asyncio.Task object for the wait_random coroutine.
    """
    coro: Coroutine = wait_random(max_delay)
    task: asyncio.Task = asyncio.create_task(coro)
    return task
