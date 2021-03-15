#!/usr/bin/env python3
""""
Module for 8. Complex types - functions.
0x00. Python - Variable Annotations
Holberton Web Stack programming Spec ― Back-end
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Parameters
    ----------
        multiplier : float
    Returns
    -------
        multiply : function (closure)
            Multiplies a float by multiplier
    """
    def multiply(num: float):
        """
        Parameters
        ----------
            num : float
        Returns
        -------
            float: Result of num * multiplier multiplication
        """
        return num * multiplier

    return multiply
