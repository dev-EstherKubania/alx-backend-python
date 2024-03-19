#!/usr/bin/env python3
"""
Module to measure the runtime of async_comprehension coroutine execution
"""
import asyncio
from typing import List
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine to execute async_comprehension four times in parallel 
    Returns:
        float: Total runtime in seconds.
    """
    start_time = perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = perf_counter()
    return end_time - start_time
