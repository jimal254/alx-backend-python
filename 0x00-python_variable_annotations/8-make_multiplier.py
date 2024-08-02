#!/usr/bin/env python3
""" 8-make_multiplier.py """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """_summary_

    Args:
        multiplier (float): _description_

    Returns:
        Callable: _description_
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
