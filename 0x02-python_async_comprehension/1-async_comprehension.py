#!/usr/bin/env python3
"""
Module to demonstrate async comprehension in Python
"""
from typing import List
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension

    Returns:
        List[float]: List of 10 random numbers.
    """
    return [num async for num in async_generator()]
