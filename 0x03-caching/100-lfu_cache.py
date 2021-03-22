#!/usr/bin/env python3
"""
Module for 100.
0x03. Caching
Holberton Web Stack programming Spec ― Back-end
"""
from collections import deque

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Defines a the class LFUCache, which inherits from BaseCaching
    and is a caching system (LFUCache).
    """
    def __init__(self):
        super().__init__()
        self.__queue = deque()
        self.__items_count = {}

    def put(self, key, item):
        """
        Assigns to the dictionary `self.cache_data` the `item` value
        for the key `key`.
        """
        if key and item:
            if key in self.cache_data:
                self.__items_count[key] += 1
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.discard()

            if key not in self.cache_data:
                self.__items_count[key] = 1

            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in `self.cache_data` linked to `key`
        or `None` if the key doesn’t exist in `self.cache_data`.
        Keeps track of used items.
        """
        if key in self.cache_data:
            self.__items_count[key] += 1
            return self.cache_data.get(key)
        return None

    def discard(self):
        """
        Discards item according cache replacement policies: LFUCache
        """
        removed = self.least_frequent()
        del self.cache_data[removed]
        del self.__items_count[removed]
        print(f"DISCARD: {removed}")

    def least_frequent(self):
        """
        Returns the least frequent used item
        """
        LFU = min([value for value in self.__items_count.values()])
        for key in self.__items_count.keys():
            if self.__items_count[key] == LFU:
                return key
