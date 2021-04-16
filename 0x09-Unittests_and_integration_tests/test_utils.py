#!/usr/bin/env python3
"""
Module for test_utils.py
0x09. Unittests and Integration Tests
Holberton Web Stack programming Spec ― Back-end
"""
import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, "a", {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, "a"),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that an exception is raised when `callable` is called with
        any positional or keyword arguments that are also passed to
        `assertRaises()`.
        The test passes if exception is raised, is an error if another
        exception is raised, or fails if no exception is raised.
        """
        with self.assertRaises(KeyError) as exception_context_manager:
            access_nested_map(nested_map, path)
