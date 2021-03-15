#!/usr/bin/env python3
""""
Module for 7. Complex types - string and int/float to tuple.
0x00. Python - Variable Annotations
Holberton Web Stack programming Spec ― Back-end
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Parameters
    ----------
        k : str
        v : int OR float
    Returns
    -------
    tuple
        The first element of the tuple is the string `k`.
        The second element is the square of the int/float `v`
        and should be annotated as a float.
    """
    return (k, v * v)
