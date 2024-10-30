#!/usr/bin/env python3
"""This module create a FIFOCache.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching
    and uses FIFO caching """

    def __init__(self):
        """Initialize the FIFOCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache following FIFO principle
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """Get an item by key
        """
        return self.cache_data.get(key, None)
