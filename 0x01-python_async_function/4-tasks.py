#!/usr/bin/env python3
"""
This module demonstrates how to run multiple tasks concurrently
and gather their results in Python using asyncio.
"""

import asyncio
from typing import List

# Import task_wait_random from the previous file
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay for task_wait_random.

    Returns:
        List[float]: A list of the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)


if __name__ == "__main__":
    # Test the task_wait_n function with different parameters
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
