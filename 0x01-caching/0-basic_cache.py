#!/usr/bin/env python3

'''
Task 0 Basic Dictionary
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    A class that inherits from the Basecaching and is a caching system
    '''

    def put(self, key, item):
        '''
        Assign to the dictionary
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        Return the value in linked to key
        '''

        return self.cache_data.get(key None)
