#!/usr/bin/env python3
"""Module for task 9"""


def insert_school(mongo_collection, **kwargs):
    """It inserts a new document"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
