#!/usr/bin/env python3
""""
Module for 11. More involved type annotations.
0x00. Python - Variable Annotations
Holberton Web Stack programming Spec ― Back-end
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None]
                     ) -> Union[Any, T]:
    """Method that gets a value of a dictionary according to `key`"""
    if key in dct:
        return dct[key]
    else:
        return default
