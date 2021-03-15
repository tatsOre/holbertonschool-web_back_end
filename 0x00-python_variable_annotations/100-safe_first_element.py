#!/usr/bin/env python3
""""
Module for 10. Duck typing - first element of a sequence.
0x00. Python - Variable Annotations
Holberton Web Stack programming Spec ― Back-end
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Method that returns the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
