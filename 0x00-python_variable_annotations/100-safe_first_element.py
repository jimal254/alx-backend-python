#!/usr/bin/env python3
""" 100-safe_first_element.py """

from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """_summary_

    Args:
        lst (Sequence[Any]): _description_

    Returns:
        Union[Any, None]: _description_
    """
    if lst:
        return lst[0]
    else:
        return None
