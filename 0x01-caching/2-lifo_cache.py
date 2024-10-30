#!/usr/bin/env python3
"""This module create a Last In First Out Cache.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching
    and uses LIFO caching
    """

    def __init__(self):
        """Initialize the LIFOCache
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item in the cache following LIFO principle
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key in self.cache_data:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")
            self.last_key = key

    def get(self, key):
        """Get an item by key
        """
        return self.cache_data.get(key, None)
