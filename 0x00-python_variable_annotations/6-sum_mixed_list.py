#!/usr/bin/env python3
""""
Module for 6. Complex types - mixed list.
0x00. Python - Variable Annotations
Holberton Web Stack programming Spec ― Back-end
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Method that takes a list mxd_lst of integers
    and floats and returns their sum as a float
    """
    return sum(mxd_lst)
