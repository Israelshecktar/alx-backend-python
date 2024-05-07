#!/usr/bin/env python3
"""
This module demonstrates how to measure the execution time of
asynchronous functions in Python using asyncio and the time module.
"""

import asyncio
import time
from typing import Callable

# Import wait_n from the previous file
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns the
    average time per call.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        float: The average time per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    # Test the measure_time function with different parameters
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
