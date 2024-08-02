#!/usr/bin/env python3
""" 5-sum_list.py """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum_list which takes a list input_list of floats
    as argument and
    returns their sum as a float.
    """
    sum: float = 0
    for i in range(len(input_list)):
        sum += input_list[i]

    return sum
