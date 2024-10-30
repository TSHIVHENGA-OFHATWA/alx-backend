#!/usr/bin/env python3
"""This module create a Least Frequent Used Cache.
"""
from .base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class that inherits from BaseCaching
        and uses LFU caching
    """

    def __init__(self):
        """Initialize the LFUCache
        """
        super().__init__()
        self.freq = {}
        self.access_order = []

    def put(self, key, item):
        """Add an item in the cache following LFU principle
        """
        if key is None or item is None:
            return

        # Update item in cache or add a new one
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.access_order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq.values())
                least_frequent_keys = [
                        k for k in self.access_order if self.freq[k] == min_freq
                        ]
                # Discard the LRU item among the least frequent
                lfu_key = least_frequent_keys[0]
                self.access_order.remove(lfu_key)
                del self.cache_data[lfu_key]
                del self.freq[lfu_key]
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.freq[key] = 1

        # Update access order for LRU and usage frequency
        self.access_order.append(key)

    def get(self, key):
        """Get an item by key, updating its frequency and access order
        """
        if key is None or key not in self.cache_data:
            return None
        # Update frequency and move key to end of access order
        self.freq[key] += 1
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
