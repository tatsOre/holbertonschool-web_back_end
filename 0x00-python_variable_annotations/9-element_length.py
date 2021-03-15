#!/usr/bin/env python3
""""
Module for 9. Let's duck type an iterable object.
0x00. Python - Variable Annotations
Holberton Web Stack programming Spec ― Back-end
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Method that takes a list as argument and returns
    tuples of item/length of every list element
    """
    return [(i, len(i)) for i in lst]
