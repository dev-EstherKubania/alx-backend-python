#!/usr/bin/env python3
"""
Module to demonstrate asyncio Tasks in Python
"""
import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that takes an integer max_delay and returns an asyncio

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: An asyncio.Task object for the wait_random coroutine.
    """
    # Calling wait_random to create a coroutine
    coro: Coroutine = wait_random(max_delay)
    # Creating an asyncio.Task object for the coroutine
    task: asyncio.Task = asyncio.create_task(coro)
    return task
