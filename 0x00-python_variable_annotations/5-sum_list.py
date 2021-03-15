#!/usr/bin/env python3
""""
Module for 5. Complex types - list of floats.
0x00. Python - Variable Annotations
Holberton Web Stack programming Spec ― Back-end
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
  """
  Method that takes a list `input_list` of floats as argument
  and returns their sum as a float
  """
  return sum(input_list)
