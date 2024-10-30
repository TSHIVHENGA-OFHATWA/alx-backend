#!/usr/bin/env python3
"""This module create a Most Recently Used Cache.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that inherits from BaseCaching
    and uses MRU caching
    """

    def __init__(self):
        """Initialize the MRUCache
        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """Add an item in the cache following MRU principle"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # Remove the existing key to update its position
                self.access_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the most recently used item
                mru_key = self.access_order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            # Add item to the cache and update access order
            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        """Get an item by key, updating the access order
        """
        if key in self.cache_data:
            # Move accessed key to the end to mark it as recently used
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
