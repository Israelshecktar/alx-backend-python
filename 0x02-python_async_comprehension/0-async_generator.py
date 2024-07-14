#!/usr/bin/env python3
"""Async Generator"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """Yield random numbers between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()
