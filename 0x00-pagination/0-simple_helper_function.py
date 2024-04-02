#!/usr/bin/env python3

"""
ALX task 0 Simple helper function
"""


def index_range(page, page_size):
    """
    Returns a tuple containing the start and end index for pagination.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
