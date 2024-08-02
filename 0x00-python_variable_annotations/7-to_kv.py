#!/usr/bin/env python3
""" 7-to_kv.py """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """_summary_

    Args:
        k (str): STR
        v (Union[int, float]): Int OR float 

    Returns:
        Tuple: _description_
    """
    v = v ** 2
    return (k, v)
