#!/usr/bin/env python3
"""
Module for test_utils.py
0x09. Unittests and Integration Tests
Holberton Web Stack programming Spec ― Back-end
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ Defines the TestAccessNestedMap Class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that utils.access_nested_map returns the expected result
        """
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


class TestGetJson(unittest.TestCase):
    """ Defines the TestGetJson Class """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that utils.get_json returns the expected result
        """
        response = Mock()
        response.json.return_value = test_payload
        with patch('requests.get', return_value=response) as mock_get:
            self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
        """
