#!/usr/bin/env python3
"""
This module provides a basic example of asynchronous programming
with asyncio and the random module in Python.
"""


import asyncio
import random
from typing import Generator

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max

    Args:
        max_delay (int): The maximum delay time in seconds.

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    # Test the wait_random coroutine
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
